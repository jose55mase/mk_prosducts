from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar

from app.services.SplanesCategory import SplanesCategory
from app.models.Mproduct import ModelProduct

import json
import time
import collections

class RplanesCategory(resource):
    """docstring for RplanesCategory."""

    def __init__(self):
        pass

    def get(self):
        objectoJson = {'Mensaje':None,'Resultados':[]}

        try:
            requestReturn = SplanesCategory().GET_ALL_PUBLIC_CATEGORY()
            listJson = json.dumps(requestReturn)

            jsonTemplate = response(listJson,status=200, mimetype='application/json')
            jsonTemplate.headers['Access-Control-Allow-Origin'] = '*'
            print("____________________________________")
            print(jsonTemplate)
            print("____________________________________")
            print("Process select OK")
            return jsonTemplate
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500
