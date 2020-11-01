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
pokemon_collection = mongo.Pokemon_Table


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
                        "Type1":"The first type of this Pokemon",
                        "Type2":"The second type of this Pokemon",
                        'HP':'The initial HP points for this Pokemon',
                        'ATK':'The initial ATK points for this Pokemon',
                        'DEF':'The initial DEF points for this Pokemon',
                        'SP_ATK':'The initial SP_ATK points for this Pokemon',
                        'SP_DEF':'The initial SP_DEF points for this Pokemon',
                        'SPD':'The initial SPD points for this Pokemon',
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

    return render_template(templates["home"])


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
    The type list.

    Returns
    -------
    A list of pokemon type
    """
    type_document=pokemon_collection.find({"Search_Id":'type_list'})['Type_list']
    



########################################
# RUN FLASK
########################################

if __name__ == "__main__":
    app.run(debug=True)

