#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
from flask import jsonify, request
import json
import time
#from flask_sqlalchemy import SQLAlchemy

#   Operaciones SQL  con categorias
class Susers:
    #   constructor
    def __init__(self):
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass


    #   Trae la lista de  productos
    def GET_ALL_USERS (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "SELECT * FROM users"
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        #   Se recorre los resultados y se guardan en un array
        array = [] #    El array de retorno
        print(resultado)
        json = {        }
        for row in resultado:
            json["id"] = row.id
            json["email"] = row.email               
            array.append(json)
            json = {}
        return array