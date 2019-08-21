#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
from flask import jsonify, request
import json
import time
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
            #,Stock_Actual = 0
            #,Stock_Limite = 0
            ,Estado = 0
            ,Peso = 0
            ,Alto = 0
            ,Largo = 0
            ,Ancho = 0
            ,Color = " "
            ,Talla = 0
            ,Creado_Por = 0
            ,Modificado_Por = 0
            ,Fecha_Creacion = None
            ,Fecha_Actualizacion = None
            ,SKU = 0
            #,informacion = ""
            ,Imagenes_1 = None
            #,Imagenes_2 = None
            #,Imagenes_3 = None
            #,Imagenes_4 = None
            #,Imagenes_5 = None
            #,Imagenes_6 = None
            #,Imagenes_7 = None

        ):
        """ Campos """
        self.__Producto_Id = Producto_Id
        self.__Categoria_id = Categoria_id
        self.__Titulo = Titulo
        self.__Precio = Precio
        self.__Precio_Descuento = Precio_Descuento
        #self.__Stock_Actual = Stock_Actual
        #self.__Stock_Limite = Stosk_Limite
        self.__Descripcion = Descripcion
        self.__Estado = Estado
        self.__Peso = Peso
        self.__Alto = Alto
        self.__Largo = Largo
        self.__Ancho = Ancho
        self.__Color = Color
        self.__Talla = Talla
        self.__Creado_Por = Creado_Por
        self.__Modificado_Por = Modificado_Por
        self.__Fecha_Creacion = Fecha_Creacion if Fecha_Creacion is not None else time.strftime("%c")
        self.__Fecha_Actualizacion = Fecha_Actualizacion
        self.__SKU = SKU
        self.__Imagenes_1 = Imagenes_1


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
        print(resultado)
        json = {        }
        for row in resultado:
            json["Product_id"] = row.Producto_Id
            json["Categoria_id"] = row.Categoria_id
            json["titulo"] = row.Titulo           
            json["Descripcion"] = row.Descripcion
            json["Peso"] = row.Peso
            json["Largo"] = row.Largo
            json["Estado"] = row.Estado
            json["Color"] = row.Color
            json["Alto"] = row.Alto
            json["Ancho"] = row.Ancho
            json["Talla"] = row.Talla
            json["Precio"] = row.Precio
            json["Precio_Descuento"] = row.Precio_Descuento
            json["Creado_Por"] = row.Creado_Por
            json["Modificado_Por"] = row.Modificado_Por
            json["Fecha_Creacion"] = row.Fecha_Creacion
            json["SKU"] = row.SKU
            array.append(json)
            json = {}
        return array
   
    # Insertar producto
    def INSERT_PRODUCT(self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        
        sql = "INSERT INTO tbl_Productos_pruebas_mk (Categoria_id,Titulo,Descripcion,Precio,Precio_Descuento,\
            Estado,Peso,Alto,Largo,Ancho,Color,Talla,Creado_Por,Modificado_Por,Fecha_Creacion,Fecha_Actualizacion,SKU) \
            \
            VALUES ('{Categoria_id}','{Titulo}','{Descripcion}','{Precio}','{Precio_Descuento}','{Estado}',\
            '{Peso}','{Alto}','{Largo}','{Ancho}','{Color}','{Talla}','{Creado_Por}','{Modificado_Por}',\
            '{Fecha_Creacion}','{Fecha_Actualizacion}','{SKU}')".format(
            Producto_Id = self.__Producto_Id
            ,Categoria_id = self.__Categoria_id
            ,Titulo = self.__Titulo
            ,Precio = self.__Precio
            ,Precio_Descuento = self.__Precio_Descuento
            # ,Stock_Actual = self.__Stock_Actual
            # ,Stosk_Limite = self.__Stock_Limite
            ,Descripcion = self.__Descripcion
            ,Estado = self.__Estado
            ,Peso = self.__Peso
            ,Alto = self.__Alto
            ,Largo = self.__Largo
            ,Ancho = self.__Ancho
            ,Color = self.__Color
            ,Talla = self.__Talla
            ,Creado_Por = self.__Creado_Por
            ,Modificado_Por = self.__Modificado_Por
            ,Fecha_Creacion = self.__Fecha_Creacion 
            ,Fecha_Actualizacion = self.__Fecha_Actualizacion
            ,SKU = self.__SKU
            )
        print(sql)
        print("Estado de insercion : Ok ")
        #cursor.execute(sql)

        return {"Status":" Ok "}
    # Actualizaer produrctos
    def UPDATE_PRODUCT(self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()        
        sql = "UPDATE tbl_Productos_pruebas_mk SET Categoria_id='{Categoria_id}',Titulo='{Titulo}',Descripcion='{Descripcion}',\
            Precio='{Precio}',Precio_descuento='{Precio_Descuento}',Estado='{Estado}',Peso='{Peso}',Alto='{Alto}',Largo='{Largo}',Ancho='{Ancho}',\
            Color='{Color}',Talla='{Talla}',Creado_Por='{Creado_Por}',Modificado_Por='{Modificado_Por}',\
            Fecha_Creacion='{Fecha_Creacion}',Fecha_Actualizacion='{Fecha_Actualizacion}',SKU='{SKU}'\
            WHERE Producto_Id = '{Producto_Id}'".format(  
           Producto_Id = self.__Producto_Id
            ,Categoria_id = self.__Categoria_id
            ,Titulo = self.__Titulo
            ,Precio = self.__Precio
            ,Precio_Descuento = self.__Precio_Descuento
            # ,Stock_Actual = self.__Stock_Actual
            # ,Stosk_Limite = self.__Stock_Limite
            ,Descripcion = self.__Descripcion
            ,Estado = self.__Estado
            ,Peso = self.__Peso
            ,Alto = self.__Alto
            ,Largo = self.__Largo
            ,Ancho = self.__Ancho
            ,Color = self.__Color
            ,Talla = self.__Talla
            ,Creado_Por = self.__Creado_Por
            ,Modificado_Por = self.__Modificado_Por
            ,Fecha_Creacion = self.__Fecha_Creacion 
            ,Fecha_Actualizacion = self.__Fecha_Actualizacion
            ,SKU = self.__SKU
        )
        
        cursor.execute(sql)
        print("Status : Ok ")
        return {"Status":" Ok "}
   
   
   
   
        # Eliminar productos ( Estado 2 )
    # Eliminar producto
    def DELETE_PRODUCT(self):
        conexion = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "UPDATE tbl_Productos_pruebas_mk SET Estado = 1 WHERE Producto_Id = '{Producto_Id}' AND Estado = 1".format(
            Producto_Id = self.__Producto_Id
            ,Estado=self.__Estado
        )
        print("Hoy Product_id",sql)
        cursor.execute(sql)
    # Parar producto ( Estado 0 )
    def STOP_PRODUCT(self):
        conexion = pyodbc.connect(self.__constring,autocommit=True,timeout=10)
        cursor = conexion.cursor()
        sql = "UPDATE tbl_Productos_pruebas_mk SET Estado = '{Estado}' WHERE Producto_Id = '{Producto_Id}'".format(
            Producto_Id = self.__Producto_Id
            ,Estado = self.__Estado
        )
        cursor.execute(sql)
        print("SQL : ",sql)

    def IMG():
        try:
            filename = None
            array_img = []      
            
            # check if the post request has the file part
            
            # if request.method == 'POST':
                #print(request.files.getlist("file"))
            
            if 'file' not in request.files:
                flash('No file part')
            
            file = request.files['file']
            
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename != '':
                if not allowed_file(file.filename):
                    return response(render_template('index.html', mimetype='text/html'))
                if file and allowed_file(file.filename):
                    extracted_format = (file.filename).split('.')

                    new_name = re.sub('[^A-Za-z0-9]+', '', extracted_format[0])

                    filename = secure_filename(new_name + '.' + extracted_format[1])

                    full_path= '/home/coder/Downloads/repository'
                    file.save(os.path.join(full_path, filename))
                    array_img = (full_path, filename)

            _filename = filename 
            
            return Response(render_template('index.html', name = name ,mimetype='txt/html'))
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno,e)