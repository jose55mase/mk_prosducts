#   Modulos de python
import pyodbc
from app.controller.connectionString import return_conection_string
#   Operaciones SQL  con categorias
class sCategorias: 
    #   constructor
    def __init__(self,nombre_Categoria=None,id_Categoria_Padre=None):
        self.__nombre_Categoria = None
        self.__id_Categoria_padre = None
        self.__constring = return_conection_string(argument='mssql', db_database='stupid_category')
        #self.__constring = connectionString().connectionODBC() #    Conexion a la base de datos.
        pass

    #   Trae todas las categorias del productos 
    def SP_GET_CATEGORIES (self):
        conexion  = pyodbc.connect(self.__constring,autocommit=True,timeout=10) # Le digo que cierre automaticamente la conexion
        cursor = conexion.cursor()
        resultado = None
        with conexion:
            sentencia = "EXEC SP_GET_CATEGORIES"
            cursor.execute(sentencia)
            resultado = cursor.fetchall()
        #   Se recorre los resultados y se guardan el un array
        array = [] #    El array de retorno 
        json = {        }
        for row in resultado:
                       
            json['id_Categoria'] = row.Categoria_id
            json['nombre_Categoria'] = row.nombre_Categoria
            json['level'] = row.level
            json['imagen'] = row.imagen
            array.append(json)
            json = {}        
        return array
    