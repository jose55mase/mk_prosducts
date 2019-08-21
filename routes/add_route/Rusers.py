#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar

from app.services.Susers import Susers

import json
import time
import collections


#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios
# from app.services.connect_to_mysql import mysql


class Rusers(resource):

    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
    # Se optiene la lista de productos
    def get(self):
        objectoJson = {'Mensaje':None,'Resultados':[]}
        try:
            retorno = Susers().GET_ALL_USERS()
            listaJson = json.dumps(retorno)
            jsonTemplate = response(listaJson,status=200, mimetype='application/json')
            jsonTemplate.headers['Access-Control-Allow-Origin'] = '*'
            print("Process select OK")
            return jsonTemplate
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500