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


class Rproduct(resource):
    def __init__(self):
        #   Se aniaden los parametros que se van a utilizar
        pass
    # Se optiene la lista de productos    
    def get(self):
        objectoJson = {'Mensaje':None,'Resultados':[]}
        try:
            retorno = Sproducts().GET_ALL_PRODUCTS()
            listaJson = json.dumps(retorno)
            jsonTemplate = response(listaJson,status=200, mimetype='application/json')
            jsonTemplate.headers['Access-Control-Allow-Origin'] = '*'
            print("Process select OK")
            return jsonTemplate
        except Exception as exp:
            print(exp)
            return {'Mensaje':'Problema interno'},500

    # Se edita o  Inserta un registro
    def post(self, *args, **kwargs):
        try:
            methdPost = request.get_json()# Datos de entrada

            methdPost.setdefault('Producto_Id', -1)
            Categoria_id=methdPost["Categoria_id"]
            Titulo= methdPost["Titulo"]
            Descripcion= methdPost["Descripcion"]
            Precio= methdPost["Precio"]
            Precio_Descuento= methdPost["Precio_Descuento"]
            Stock_Actual = methdPost[" Stock_Actual"]
            Stock_Limite= methdPost["Stock_Limite"]
            Estado= methdPost["Estado"]
            Referencia_Amazon= methdPost["Referencia_Amazon"]
            Peso= methdPost["Peso"]
            Alto= methdPost["Alto"]
            Largo= methdPost["Largo"]
            Ancho= methdPost["Ancho"]
            Color= methdPost["Color"]
            Talla= methdPost["Talla"]
            Porcentaje = methdPost[" Porcentaje"]
            Precio_cop= methdPost["Precio_cop"]
            Creado_Por= methdPost["Creado_Por"]
            Modificado_Por= methdPost["Modificado_Por"]
            Fecha_Creacion= methdPost["Fecha_Creacion"]
            Fecha_Actualizacion = methdPost["Fecha_Actualizacion"]
            Codigo= methdPost["Codigo"]
            breadcrum= methdPost[" breadcrum"]
            GUID= methdPost["GUID"]
            SKU= methdPost["SKU"]
            informacion= methdPost["informacion"]
            Imagenes_1= methdPost["Imagenes_1"]
            Imagenes_2= methdPost["Imagenes_2"]
            Imagenes_3= methdPost["Imagenes_3"]
            Imagenes_4= methdPost["Imagenes_4"]
            Imagenes_5= methdPost["Imagenes_5"]
            Imagenes_6= methdPost["Imagenes_6"]
            Imagenes_7= methdPost["Imagenes_7"]

            # Actualizar
            if int(methdPost['Producto_Id']) >= 0:
                Producto_Id =  methdPost['Producto_Id']
                Sproducts(
                    Categoria_id=Categoria_id
                    ,Titulo=Titulo
                    ,Descripcion=Descripcion
                    ,Precio=Precio
                    ,Precio_Descuento=Precio_Descuento
                    ,Stock_Actual = Stock_Actual
                    ,Stock_Limite=Stock_Limite
                    ,Estado=Estado
                    ,Referencia_Amazon=Referencia_Amazon
                    ,Peso=Peso
                    ,Alto=Alto
                    ,Largo=Largo
                    ,Ancho=Ancho
                    ,Color=Color
                    ,Talla=Talla
                    ,Porcentaje = Porcentaje
                    ,Precio_cop=Precio_cop
                    ,Creado_Por=Creado_Por
                    ,Modificado_Por=Modificado_Por
                    ,Fecha_Creacion=Fecha_Creacion
                    ,Fecha_Actualizacion =Fecha_Actualizacion
                    ,Codigo=Codigo
                    ,breadcrum= breadcrum
                    ,GUID=GUID
                    ,SKU=SKU
                    ,informacion=informacion
                    ,Imagenes_1=Imagenes_1
                    ,Imagenes_2=Imagenes_2
                    ,Imagenes_3=Imagenes_3
                    ,Imagenes_4=Imagenes_4
                    ,Imagenes_5=Imagenes_5
                    ,Imagenes_6=Imagenes_6
                    ,Imagenes_7=Imagenes_7
                ).UPDATE_PRODUCT()
                return{'Mensaje':'Producto  actualizado'}
            else:
            # Insertar
                Sproducts(
                    Categoria_id=Categoria_id
                    ,Titulo=Titulo
                    ,Descripcion=Descripcion
                    ,Precio=Precio
                    ,Precio_Descuento=Precio_Descuento
                    ,Stock_Actual = Stock_Actual
                    ,Stock_Limite=Stock_Limite
                    ,Estado=Estado
                    ,Referencia_Amazon=Referencia_Amazon
                    ,Peso=Peso
                    ,Alto=Alto
                    ,Largo=Largo
                    ,Ancho=Ancho
                    ,Color=Color
                    ,Talla=Talla
                    ,Porcentaje = Porcentaje
                    ,Precio_cop=Precio_cop
                    ,Creado_Por=Creado_Por
                    ,Modificado_Por=Modificado_Por
                    ,Fecha_Creacion=Fecha_Creacion
                    ,Fecha_Actualizacion =Fecha_Actualizacion
                    ,Codigo=Codigo
                    ,breadcrum= breadcrum
                    ,GUID=GUID
                    ,SKU=SKU
                    ,informacion=informacion
                    ,Imagenes_1=Imagenes_1
                    ,Imagenes_2=Imagenes_2
                    ,Imagenes_3=Imagenes_3
                    ,Imagenes_4=Imagenes_4
                    ,Imagenes_5=Imagenes_5
                    ,Imagenes_6=Imagenes_6
                    ,Imagenes_7=Imagenes_7
                ).INSERT_PRODUCT()
                return{'Mensaje':'Producto  Insertado'}

            # Pausar
            if methdPost["Estado"] == 2:
                methdPost = request.get_json()
                Producto_Id = methdPost['Producto_Id']
                Sproducts(
                    Producto_Id = Producto_Id
                ).DELETE_PRODUCT()
                print("Producto pausardo ( estado = 0 )")
                return{'Mensaje':'Producto  se Pauso'}

        except Exception as error:
            print(error)
            return {'Mensaje':'Problema interno'},500

    def delete(self, *args, **kwargs):
            try:
                methdPost = request.get_json()
                Producto_Id = methdPost['Producto_Id']
                Sproducts(
                    Producto_Id = Producto_Id
                ).DELETE_PRODUCT()
                print("Producto eliminado ( estado = 1 )")
                return{'Mensaje':'Producto  Eliminado'}
            except Exception as error:
                print(error)
                return {'Mensaje':'Problema interno'},500