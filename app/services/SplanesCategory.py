import pyodbc
from app.controller.connectionString import return_conection_string
from flask import jsonify, request
import json
import time

class SplanesCategory:
    """docstring for SplanesCategory."""

    def __init__(self):
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass

    def GET_ALL_PUBLIC_CATEGORY(self):
        connection = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = connection.cursor()
        requestsHandle = None


        #sql = "SELECT id,name,parent_id FROM public_categories WHERE parent_id IS NULL"
        sql = "SELECT id,name,parent_id FROM public_categories"
        cursor.execute(sql)
        requestsHandle = cursor.fetchall()

        _array = []
        _json = {}

        for element in requestsHandle:
            _json["id"] = element.id
            _json["name"] = element.name
            _json["parent_id"] = element.parent_id
            _array.append(_json)
            _json = {}
        return _array
