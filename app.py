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



########################################
# CONSTANTS
########################################

api_current_version = "v1.0"

routes = {
    "home": "/",
    "api_versions": "/api",
    "api_docs": "/api/<version>",
}

templates = {
    "home": "index.html",
    "api_docs": "api_docs.html",
    "api_versions": "api_versions.html"
}


version_infos=[
    {
        "name":"v1.0",
        "url":"/api/v1.0",
        "documentation":{
            "/api/v1.0/type":"Gets a list of available pokemon types.",
            "/api/v1.0/type/<type>":[
                {
                    "Type" : {
                        'Damaged Normally by':'A list of type this Pokemon is damaged noramlly by.',
                        'Weak to':'A list of type this Pokemon is weak to.',
                        'Immue to':'A list of type this Pokemon is immue to.',
                        'Resisant to':'A list of type this Pokemon is resistan to.'
                    }
                }
            ],
            "/api/v1.0/name":"Gets a list of available Pokemon names.",
            "/api/v1.0/name/<name>":[
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


@app.route(routes["api_versions"])
def api_version():
    """
    Shows the documentation for a specific API.

    Parameters
    ----------
    version : string
        The API version to show.

    Returns
    -------
    Flask Rendered Template :
        The HTML to show.
    """
    return jsonify(version_infos[0]['documentation'])

@app.route(routes["api_docs"])
def api_docs():
    """
    The homepage.

    Returns
    -------
    Flask Rendered Template :
        The HTML to show.
    """

    return render_template(templates["home"])



if __name__ == "__main__":
    app.run(debug=True)

