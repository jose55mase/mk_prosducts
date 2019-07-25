#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
from flask import jsonify, request
import json
#from flask_sqlalchemy import SQLAlchemy

#   Operaciones SQL  con categorias
class Sproducts:
    #   constructor
    def __init__(self
            ,Producto_Id = 0
            ,Categoria_id=0
            ,Titulo= " "
            ,Descripcion=" "
            ,Precio = 0
            ,Precio_Descuento = 0
            ,Stock_Actual = 0
            ,Stock_Limite = 0
            ,Estado = 0
            ,Referencia_Amazon = " "
            ,Peso = 0
            ,Alto = 0
            ,Largo = 0
            ,Ancho = 0
            ,Color = ""
            ,Talla = 0
            ,Porcentaje = 0
            ,Precio_cop = 0
            ,Creado_Por = 0
            ,Modificado_Por = 0
            ,Fecha_Creacion = None
            ,Fecha_Actualizacion = None
            ,Codigo = 0
            ,breadcrum = ""
            ,GUID = ""
            ,SKU = 0
            ,informacion = ""
            ,Imagenes_1 = None
            ,Imagenes_2 = None
            ,Imagenes_3 = None
            ,Imagenes_4 = None
            ,Imagenes_5 = None
            ,Imagenes_6 = None
            ,Imagenes_7 = None
        ):
        """ Campos """
        self.__Producto_Id = Producto_Id
        self.__Categoria_id = Categoria_id
        self.__Titulo = Titulo
        self.__Descripcion = Descripcion
        self.__Precio = Precio
        self.__Precio_Descuento = Precio_Descuento
        self.__Stock_Actual = Stock_Actual
        self.__Stock_Limite = Stock_Limite
        self.__Estado = Estado
        self.__Referencia_Amazon = Referencia_Amazon
        self.__Peso = Peso
        self.__Alto = Alto
        self.__Largo = Largo
        self.__Ancho = Ancho
        self.__Color = Color
        self.__Talla = Talla
        self.__Porcentaje = Porcentaje
        self.__Precio_cop = Precio_cop
        self.__Creado_Por = Creado_Por
        self.__Modificado_Por = Modificado_Por
        self.__Fecha_Creacion = Fecha_Creacion
        self.__Fecha_Actualizacion = Fecha_Actualizacion
        self.__Codigo = Codigo
        self.__breadcrum = breadcrum
        self.__GUID = GUID
        self.__SKU = SKU
        self.__informacion = informacion
        self.__Imagenes_1 = Imagenes_1 if Imagenes_1 is not None else 'Sin imagen'
        self.__Imagenes_2 = Imagenes_2 if Imagenes_2 is not None else 'Sin imagen'
        self.__Imagenes_3 = Imagenes_3 if Imagenes_3 is not None else 'Sin imagen'
        self.__Imagenes_4 = Imagenes_4 if Imagenes_4 is not None else 'Sin imagen'
        self.__Imagenes_5 = Imagenes_5 if Imagenes_5 is not None else 'Sin imagen'
        self.__Imagenes_6 = Imagenes_6 if Imagenes_6 is not None else 'Sin imagen'
        self.__Imagenes_7 = Imagenes_7 if Imagenes_7 is not None else 'Sin imagen'
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        pass
        

    #   Trae la lista de  productos
    def GET_ALL_PRODUCTS (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "SELECT * FROM tbl_Productos_pruebas_mk"
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        #   Se recorre los resultados y se guardan en un array
        array = [] #    El array de retorno
        json = {        }
        for row in resultado:
            json["titulo"] = row.Titulo
            array.append(json)
            json = {}
        return array

    # Insertar producto
    def INSERT_PRODUCT(self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "INSERT INTO tbl_Productos_pruebas_mk  VALUES ('{Categoria_id}','{Titulo}','{Descripcion}','{Precio}','{Precio_Descuento}','{Stock_Actual}','{Stock_Limite}','{Estado}','{Referencia_Amazon}','{Peso}','{Alto}','{Largo}','{Ancho}','{Color}','{Talla}','{Porcentaje}','{Precio_cop}','{Creado_Por}','{Modificado_Por}','{Fecha_Creacion}','{Fecha_Actualizacion}','{Codigo}','{breadcrum}','{GUID}','{SKU}','{informacion}','{Imagenes_1}','{Imagenes_2}','{Imagenes_3}','{Imagenes_4}','{Imagenes_5}','{Imagenes_6}','{Imagenes_7}')".format(
                    Categoria_id=self.__Categoria_id
                    ,Titulo=self.__Titulo
                    ,Descripcion=self.__Descripcion
                    ,Precio=self.__Precio
                    ,Precio_Descuento=self.__Precio_Descuento
                    ,Stock_Actual = self.__Stock_Actual
                    ,Stock_Limite=self.__Stock_Limite
                    ,Estado=self.__Estado
                    ,Referencia_Amazon=self.__Referencia_Amazon
                    ,Peso=self.__Peso
                    ,Alto=self.__Alto
                    ,Largo=self.__Largo
                    ,Ancho=self.__Ancho
                    ,Color=self.__Color
                    ,Talla=self.__Talla
                    ,Porcentaje = self.__Porcentaje
                    ,Precio_cop=self.__Precio_cop
                    ,Creado_Por=self.__Creado_Por
                    ,Modificado_Por=self.__Modificado_Por
                    ,Fecha_Creacion=self.__Fecha_Creacion
                    ,Fecha_Actualizacion =self.__Fecha_Actualizacion
                    ,Codigo=self.__Codigo
                    ,breadcrum= self.__breadcrum
                    ,GUID=self.__GUID
                    ,SKU=self.__SKU
                    ,informacion=self.__informacion
                    ,Imagenes_1=self.__Imagenes_1
                    ,Imagenes_2=self.__Imagenes_2
                    ,Imagenes_3=self.__Imagenes_3
                    ,Imagenes_4=self.__Imagenes_4
                    ,Imagenes_5=self.__Imagenes_5
                    ,Imagenes_6=self.__Imagenes_6
                    ,Imagenes_7=self.__Imagenes_7
                    )
        executeQuery = cursor.execute(sql)
        return {"Status":" Ok "}

    def UPDATE_PRODUCT(self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "UPDATE tbl_Productos_pruebas_mk SET Titulo='{Titulo}',Categoria_id='{Categoria_id}',Descripcion='{Descripcion}',Precio='{Precio}',Precio_Descuento='{Precio_Descuento}',Stock_Actual='{Stock_Actual}',Stock_Limite='{Stock_Limite}',Estado='{Estado}',Referencia_Amazon='{Referencia_Amazon}',Peso='{Peso}',Alto='{Alto}',Largo='{Largo}',Ancho='{Ancho}',Color='{Color}',Talla='{Talla}',Porcentaje='{Porcentaje}',Precio_cop='{Precio_cop}',Creado_Por='{Creado_Por}',Modificado_Por='{Modificado_Por}',Fecha_Creacion='{Fecha_Creacion}',Fecha_Actualizacion='{Fecha_Actualizacion}',Codigo='{Codigo}',breadcrum='{breadcrum}',GUID='{GUID}',SKU='{SKU}',informacion='{informacion}',Imagenes_1='{Imagenes_1}',Imagenes_2='{Imagenes_2}',Imagenes_3='{Imagenes_3}',Imagenes_4='{Imagenes_4}',Imagenes_5='{Imagenes_5}',Imagenes_6='{Imagenes_6}',Imagenes_7='{Imagenes_7}' WHERE Producto_Id = '{Producto_Id}'".format(
            Producto_Id=self.__Producto_Id
            ,Categoria_id=self.__Categoria_id
            ,Titulo=self.__Titulo
            ,Descripcion=self.__Descripcion
            ,Precio=self.__Precio
            ,Precio_Descuento=self.__Precio_Descuento
            ,Stock_Actual = self.__Stock_Actual
            ,Stock_Limite=self.__Stock_Limite
            ,Estado=self.__Estado
            ,Referencia_Amazon=self.__Referencia_Amazon
            ,Peso=self.__Peso
            ,Alto=self.__Alto
            ,Largo=self.__Largo
            ,Ancho=self.__Ancho
            ,Color=self.__Color
            ,Talla=self.__Talla
            ,Porcentaje = self.__Porcentaje
            ,Precio_cop=self.__Precio_cop
            ,Creado_Por=self.__Creado_Por
            ,Modificado_Por=self.__Modificado_Por
            ,Fecha_Creacion=self.__Fecha_Creacion
            ,Fecha_Actualizacion =self.__Fecha_Actualizacion
            ,Codigo=self.__Codigo
            ,breadcrum= self.__breadcrum
            ,GUID=self.__GUID
            ,SKU=self.__SKU
            ,informacion=self.__informacion
            ,Imagenes_1=self.__Imagenes_1
            ,Imagenes_2=self.__Imagenes_2
            ,Imagenes_3=self.__Imagenes_3
            ,Imagenes_4=self.__Imagenes_4
            ,Imagenes_5=self.__Imagenes_5
            ,Imagenes_6=self.__Imagenes_6
            ,Imagenes_7=self.__Imagenes_7
        )
        cursor.execute(sql)
        return {"Status":" Ok "}

    def DELETE_PRODUCT(self):
        conexion = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "UPDATE tbl_Productos_pruebas_mk SET Estado = 1 WHERE Producto_Id = '{Producto_Id}' AND Estado = 1".format(
            Producto_Id = self.__Producto_Id
            ,Estado=self.__Estado
        )
        cursor.execute(sql)
    
    def STOP_PRODUCT(self):
        conexion = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "UPDATE tbl_Productos_pruebas_mk SET Estado = 0 WHERE Producto_Id = '{Producto_Id}' AND Estado = 2".format(
            Producto_Id = self.__Producto_Id
            ,Estado=self.__Estado
        )
        cursor.execute(sql)