#   Clase Usuarios Rutas
#   Creada por: ...
#   Fecha creacion: ...

#Archivos necesarios para flask

#Se llama el objeto de flask
from flask import jsonify, request
from routes.router import app,resource,response,req,reqpar
#from database.schemas.catalogo import Catalogo

from app.models.mcategorias import mCategoria
from app.services.scategorias import sCategorias

import json

#Importando el conector odbc para las conexiones con mssql
import pyodbc
#clase para el control de rutas en usuarios 
# from app.services.connect_to_mysql import mysql


class get_categorias(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass

    # #validaciones de usuario
    # obtiene las categorias de la base de datos
    #   se organiza todo para generar un arbol de categorias con json.
    def __Generar_Arbol_Categorias(self,categorias):
        #print(categorias)
        if categorias is not None:
            #   Definimos las variables 
            #   tomamos las categoria padres
            lvl1 =  [{'Id Categoria':categoria['id_Categoria'],'Nombre categoria':categoria['nombre_Categoria'],'url':(str(categoria['nombre_Categoria']).lower()).replace(' ','-'),'Categorias hijas': [],'imagen_categoria':categoria['imagen']} for categoria in categorias if categoria['level'] == 1]
            json1 = [] # creamos esta variable auxiliar para guardar los valores
            for nivel1 in lvl1: # recorremos las categorias padres 
                json2 = []
                #   tomamos las categorias a partir del nombre de la categoria padre y los 
                nombrePadr = nivel1['Nombre categoria']          
                lvl2 = [{'Id Categoria':categoria['id_Categoria'],'Nombre categoria':categoria['nombre_Categoria'],'Id categoria padre':nivel1['Id Categoria'],'url':(str(categoria['nombre_Categoria']).lower()).replace(' ','-'),'Categorias hijas': [],'imagen_categoria':categoria['imagen']} for categoria in categorias if categoria['level'] == 2 and categoria['nombre_Categoria'].find(nivel1['Nombre categoria']) != -1]
                for nivel2 in lvl2:
                    nombreHija =   nivel2['Nombre categoria'] + '/'
                    lvl3 = [{'Id Categoria':categoria['id_Categoria'],'Nombre categoria':str(categoria['nombre_Categoria']).replace(nombreHija,''),'Id categoria padre':nivel2['Id Categoria'],'url':(str(categoria['nombre_Categoria']).lower()).replace(' ','-')} for categoria in categorias if categoria['level'] == 3 and categoria['nombre_Categoria'].find(nivel2['Nombre categoria']) != -1]
                    nivel2['Categorias hijas'].append(lvl3)
                    nivel2['Nombre categoria'] = str(nivel2['Nombre categoria']).replace(nombrePadr,'')
                    json2.append(nivel2)
                nivel1['Nombre categoria'] = nivel1['Nombre categoria'].replace('/','')
                nivel1['Categorias hijas'].append(json2)
                json1.append(nivel1)
            return json1
        return None
        
    def get(self):        
        mcategoria = mCategoria() # se llama al modelo
        scategorias = sCategorias() # se llaman a los servicios
        
        try:
            retorno = scategorias.SP_GET_CATEGORIES() # Se obtienen las categorias.
            category_Tree = self.__Generar_Arbol_Categorias(retorno) # se asocian las categorias y se convierten a un json.
            #Se define el metodo del retorno response
           
            objectoJson = {'Mensaje':None,'Resultados':[]}
            if (retorno is not None):
                objectoJson['Mensaje'] =  'Proceso exitoso'
                objectoJson['Resultados'] = category_Tree
                _json = json.dumps(objectoJson)
                _response = response(_json,status=200, mimetype='application/json')
                _response.headers['Access-Control-Allow-Origin'] = '*'
            else :
                objectoJson['Mensaje'] =  'Hubo un error' 
                _json = json.dumps(objectoJson)
                _response = response(_json,status=400, mimetype='application/json')
            return _response
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500 

    def options(self):
        return {'Metodos permitidos' : ['PUT','GET','POST'] }, 200, \
        { 'Access-Control-Allow-Origin': '*', \
        'Access-Control-Allow-Methods' : 'PUT,GET,POST', \
        'Access-Control-Allow-Headers': 'X-Custom-Header'   }
 