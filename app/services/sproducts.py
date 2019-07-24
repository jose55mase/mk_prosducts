#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
from flask import jsonify, request
import json
#from flask_sqlalchemy import SQLAlchemy

#   Operaciones SQL  con categorias
class sProducts:
    #   constructor
    def __init__(
                    self
                    ,Categoria_id=None
                    ,Titulo=None
                    ,Descripcion=None
                    ,Precio = None
                    ,Precio_Descuento = None
                    ,Stock_Actual = None
                    ,Stock_Limite = None
                    ,Estado = None
                    ,Referencia_Amazon = None
                    ,Peso = None
                    ,Alto = None
                    ,Largo = None
                    ,Ancho = None
                    ,Color = None
                    ,Talla = None
                    ,Porcentaje = None
                    ,Precio_cop = None
                    ,Creado_por = None
                    ,Modicado_por = None
                    ,Fecha_Creacion = None
                    ,Fecha_Actualizacion = None
                    ,Codigo = None
                    ,breadcrum = None
                    ,GUID = None
                    ,SKU = None
                    ,informacion = None
                    ,Imagenes_1 = None
                    ,Imagenes_2 = None
                    ,Imagenes_3 = None
                    ,Imagenes_4 = None
                    ,Imagenes_5 = None
                    ,Imagenes_6 = None
                    ,Imagenes_7 = None
                ):
        """ Campos """
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
        self.__Creado_por = Creado_por
        self.__Modicado_por = Modicado_por
        self.__Fecha_Creacion = Fecha_Creacion
        self.__Fecha_Actualizacion = Fecha_Actualizacion
        self.__Codigo = Codigo
        self.__breadcrum = breadcrum
        self.__GUID = GUID
        self.__SKU = SKU
        self.__informacion = informacion
        self.__Imagenes_1 = Imagenes_1
        self.__Imagenes_2 = Imagenes_2
        self.__Imagenes_3 = Imagenes_3
        self.__Imagenes_4 = Imagenes_4
        self.__Imagenes_5 = Imagenes_5
        self.__Imagenes_6 = Imagenes_6
        self.__Imagenes_7 = Imagenes_7
        self.__constring = return_conection_string(argument='mssql', db_database='DBKiero_Productos')
        #self.__constring = connectionString().connectionODBC() #    Conexion a la base de datos.
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
        #   Se recorre los resultados y se guardan el un array
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
        """ Insert """
        cursor.execute("""
        INSERT INTO tbl_Productos_pruebas_mk
                (
                    Categoria_id ,Titulo, Descripcion, Precio, Precio_Descuento, Stock_Actual, Stock_Limite
                    ,Estado ,Referencia_Amazon, Peso,Alto,Largo,Ancho,Color,Talla,Porcentaje,Precio_cop,Creado_por,Modicado_por,Fecha_Creacion,Fecha_Actualizacion,Codigo,breadcrum,GUID,SKU,informacion,imagenes_1,imagenes_2,imagenes_3,imagenes_4,imagenes_5,imagenes_6,imagenes_7
                )
        VALUES
        (
            '{Categoria_id}','{Titulo}','{Descripcion}','{Precio}','{Precio_Descuento}','{Stock_Actual}','{Stock_Limite}','{Estado}','{Referencia_Amazon}','{Peso}','{Alto}','{Largo}','{Ancho}','{Color}','{Talla}','{Porcentaje}','{Precio_cop}','{Creado_por}','{Modicado_por}','{Fecha_Creacion}','{Fecha_Actualizacion}','{Codigo}','{breadcrum}','{GUID}','{SKU}','{informacion}','{Imagenes_1}','{Imagenes_2}','{Imagenes_3}','{Imagenes_4}','{Imagenes_5}','{Imagenes_6}','{Imagenes_7}'

        )
        """.format(
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
                    ,Creado_por=self.__Creado_por
                    ,Modicado_por=self.__Modicado_por
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
                )
        return {"Estatus":" Ok "}
