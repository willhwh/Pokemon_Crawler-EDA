########################################
# IMPORTS
########################################

from flask import Flask, render_template, redirect, jsonify
from flask_pymongo import PyMongo
import pandas as pd
import os


########################################
# SETUP APPLICATION
########################################

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Prevent caching
mongo = PyMongo(app, uri="mongodb://localhost:27017/Pokemon_DB")
pokemon_collection = mongo.db.Pokemon_Table


########################################
# CONSTANTS
########################################


routes = {
    "home": "/",
    "api_docs": "/api",
    "type":'/api/type',
    "type_select":"/api/type/<type>",
    "name":'/api/name',
    "name_select":'/api/name/<name>'
}

templates = {
    "home": "index.html",
    "api_docs": "api_docs.html",
    "api_versions": "api_versions.html"
}


version_infos=[
    {
        "documentation":{
            "/api/type":"Gets a list of available pokemon types.",
            "/api/type/<type>":[
                {
                    "Type" : {
                        'Damaged Normally by':'A list of type this Pokemon is damaged noramlly by.',
                        'Weak to':'A list of type this Pokemon is weak to.',
                        'Immue to':'A list of type this Pokemon is immue to.',
                        'Resisant to':'A list of type this Pokemon is resistan to.'
                    }
                }
            ],
            "/api/name":"Gets a list of available Pokemon names.",
            "/api/name/<name>":[
                {
                    "Pokemon_Name" : {
                        "Type1":"The first type of this Pokemon.",
                        "Type2":"The second type of this Pokemon.",
                        'HP':'The initial HP points for this Pokemon.',
                        'ATK':'The initial ATK points for this Pokemon.',
                        'DEF':'The initial DEF points for this Pokemon.',
                        'SP_ATK':'The initial SP_ATK points for this Pokemon.',
                        'SP_DEF':'The initial SP_DEF points for this Pokemon.',
                        'SPD':'The initial SPD points for this Pokemon.',
                        'Damaged Normally by':'A list of type this Pokemon is damaged noramlly by.',
                        'Weak to':'A list of type this Pokemon is weak to.',
                        'Immue to':'A list of type this Pokemon is immue to.',
                        'Resisant to':'A list of type this Pokemon is resistan to.'
                    }
                }
            ]
        }
    }
]


########################################
# ROUTES
########################################

@app.route(routes["home"])
def home():
    """
    The homepage.

    Returns
    -------
    Flask Rendered Template :
        The HTML to show.
    """
    type_document=pokemon_collection.find_one({"Search_Id":'Type_List'})
    return render_template(templates["home"],type_document=type_document)


@app.route(routes["api_docs"])
def api_docs():
    """
    The api document page.

    Returns
    -------
    A jsonify documentation
    """

    return jsonify(version_infos[0]['documentation'])

@app.route(routes["type"])
def type():
    """
    The available types.

    Returns
    -------
    A list of pokemon type
    """
    #Retrieved type list from database.
    type_document=pokemon_collection.find_one({"Search_Id":'Type_List'})

    #Create type list json
    type_list={}
    types=[]
    for i in type_document["Types"]:
        types.append(i[1])
    type_list.update({"Type_List":types})

    return jsonify(type_list)

@app.route(routes["type_select"])
def type_select(type):
    """
    The detail of selected type.

    Returns
    -------
    A list of strength and weakness for selected type.
    """
    #Retrieved the <type>'s info from database.
    print(type)
    type_document=pokemon_collection.find_one({'Type': type})

    #Create jsonify data structure
    feature_dict={}
    feature_list=[]
    feature_dict.update({"Type":type_document["Type"]})

    feature_list.append({"Strong Against": type_document["Strong Against"]})
    feature_list.append({"Weak Against":type_document["Weak Against"]})
    feature_list.append({"Resistant To":type_document["Resistant To"]})
    feature_list.append({"Vulnerable To":type_document["Vulnerable To"]})

    feature_dict.update({"Detail":feature_list})
    return jsonify(feature_dict)


@app.route(routes["name"])
def name():
    """
    The available names.

    Returns
    -------
    A list of pokemon name
    """
    #Retrieved name list from database.
    name_document=pokemon_collection.find({"Search_Id":'Pokemon_List'})

    #Create name list json
    name_list={}
    names=[]
    for pokemon in name_document:
        if pokemon['Name'] not in names:
            names.append(pokemon['Name'])
    name_list.update({"Name_List":names})

    return jsonify(name_list)

@app.route(routes["name_select"])
def name_select(name):
    """
    The detail of selected (Pokemon) name.

    Returns
    -------
    The basic scores for selected (Pokemon) name.
    """
    #Retrieved the <name>'s info from database.
    name_document=pokemon_collection.find_one({"Name":name})

    #Create jsonify data structure
    feature_dict={}
    feature_list=[]
    feature_dict.update({"Name":name_document["Name"]})
    info_list=['Type1','Type2','Link','HP','ATK','DEF','SP_ATK','SP_DEF','SPD',
                'Damaged Normally by','Weak to', 'Immue to', 'Resisant to']
    for i in info_list:
        feature_list.append({i: name_document[i]})

    feature_dict.update({"Detail":feature_list})
    return jsonify(feature_dict)


########################################
# RUN FLASK
########################################

if __name__ == "__main__":
    app.run(debug=True)

