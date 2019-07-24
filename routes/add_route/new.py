#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar

from app.services.Sproducts import Sproducts

import json

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
# from app.services.connect_to_mysql import mysql


class new(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
        
    def get(self):             
        objectoJson = {'Mensaje':None,'Resultados':[]}      
        try:            
            retorno = Sproducts().GET_ALL_PRODUCTS()
            listaJson = json.dumps(retorno)
            jsonTemplate = response(listaJson,status=200, mimetype='application/json')
            jsonTemplate.headers['Access-Control-Allow-Origin'] = '*'
            print("Process OK")
            return jsonTemplate
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500 
    

    def post(self):
        try:
            methdPost = request.get_json()
            Categoria_id=methdPost["Categoria_id"]
            Titulo=methdPost["Titulo"]
            Descripcion=methdPost["Descripcion"]
            Estado=methdPost["Estado"]
            Referencia_Amazon=methdPost["Referencia_Amazon"]
            Creado_Por=methdPost["Creado_Por"]
            Modificado_Por=methdPost["Modificado_Por"]
            Fecha_Creacion=methdPost["Fecha_Creacion"]
            Fecha_Actualizacion=methdPost["Fecha_Actualizacion"]

            Sproducts(
                Categoria_id= Categoria_id
                ,Titulo=Titulo
                ,Descripcion=Descripcion
                ,Estado=Estado
                ,Referencia_Amazon=Referencia_Amazon
                ,Creado_Por=Creado_Por
                ,Modificado_Por=Modificado_Por
                ,Fecha_Creacion=Fecha_Creacion
                ,Fecha_Actualizacion=Fecha_Actualizacion
                ).INSERT_PRODUCT()
            print("Insert call")
            
        except Exception as error:
            print(error)
            return {'Mensaje':'Problema interno'},500
