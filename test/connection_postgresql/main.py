#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyodbc
import json 
from json import dumps
import re

# conn_str = (
#     "DRIVER={PostgreSQL Unicode};"
#     "DATABASE=other;"
#     "UID=odoo;"
#     "PWD=odoo;"
#     "SERVER=172.17.0.2;"
#     "PORT=5432;"
#     )
# conn = pyodbc.connect(conn_str)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=204.141.52.148;DATABASE=DBKiero_Productos;UID=MachineBaseConnect3651;PWD=H1#KotS(xh5nF+tGv')

#usted ejecuta y me envia imagenes
with conn:
    query = """select * from product_public_category order by id """
    crsr = conn.execute(query)
    rows = crsr.fetchall()
    # result = re.findall(r'\u00ed',str(rows))
    # print(result)

#   Se recorre los resultados y se guardan el un array
array = [] #    El array de retorno 
json = {        }
# Entonces la vuelta es la siguiente, asi sacamos las padres.
# jsonpadres = [{"id":row.id,"parent_path":row.parent_path,"name":row.name,"complete_name":row.complete_name,"categorias_Hijas":None} for row in rows if row.parent_id is None]
#calma

#lo que pasa es que al parecer estaba consumiendo una base de datos que no es, quiero probar a ver como me trae las categorias si le dio



jsonpadres = [{
    "id":row.id,
    "parent_path":str(row.id) + ' /',
    "name":row.name,
    "complete_name":row.name + ' /',
    "categorias_Hijas":None
} for row in rows if row.parent_id is None]


i = 0
for jsnp in jsonpadres:  
    jsonhijas = [{
        "id":row.id,
        "parent_path":str(jsnp['id']) + ' / ' + str(row.id),
        "name":row.name,
        "complete_name": jsnp['name'] + ' / ' + row.name,
        "categorias_Hijas":None
    } for row in rows if row.parent_id == jsnp['id']]


    qwe = 0
    for nietasT in jsonhijas:
        nietas = [{
            "id":row.id,
            "parent_path":str(jsnp['id']) + ' / ' + str(nietasT['id']) + ' / ' + str(row.id),
            "name":row.name,
            "complete_name":jsnp['name'] + ' / ' + nietasT['name'] + ' / ' + row.name,
            "categorias_Hijas":None
        } for row in rows if row.parent_id == nietasT['id']]


        try:                
            nivel4count = 0
            for nivel4 in nietas:
                level4 = [{
                    "id":row.id,
                    "parent_path":str(jsnp['id']) +' / ' + str(nietasT['id']) + ' / ' + str(nivel4['id']) +' / ' + str(row.id),
                    "name":row.name,
                    "complete_name":str(jsnp['name']) +' / ' + str(nietasT['name']) + ' / ' + str(nivel4['name']) +' / ' + str(row.name),
                    "categorias_Hijas":None
                } for row in rows if row.parent_id == nivel4['id']]

                nivel5count = 0
                for nivel5 in level4:
                    level5 = [{
                        "id":row.id,
                        "parent_path":str(jsnp['id']) +' / ' + str(nietasT['id']) + ' / ' + str(nivel4['id']) + ' / '+ str(nivel5['id']) +' / '+ str(row.id),
                        "name":row.name,
                        "complete_name":str(jsnp['name']) +' / ' + str(nietasT['name']) + ' / ' + str(nivel4['name']) + ' / '+ str(nivel5['name']) +' / '+ str(row.name),
                        "categorias_Hijas":None
                    } for row in rows if row.parent_id == nivel5['id']]

                    nivel6count = 0
                    for nivel6 in level5:
                        level6 = [{
                            "id":row.id,
                            "parent_path":str(jsnp['id']) +' / ' + str(nietasT['id']) + ' / ' + str(nivel4['id']) + ' / '+ str(nivel5['id']) + ' / '+ str(nivel6['id']) +' / '+ str(row.id),
                            "name":row.name,
                            "complete_name":str(jsnp['name']) +' / ' + str(nietasT['name']) + ' / ' + str(nivel4['name']) + ' / '+ str(nivel5['name']) + ' / '+ str(nivel6['name']) +' / '+ str(row.name),
                            "categorias_Hijas":None
                        } for row in rows if row.parent_id == nivel6['id']]

                        nivel7count = 0
                        for nivel7 in level4:
                            level7 = [{
                                "id":row.id,
                                "parent_path":str(jsnp['id']) +' / ' + str(nietasT['id']) + ' / ' + str(nivel4['id']) + ' / '+ str(nivel5['id']) + ' / '+ str(nivel7['id']) +' / '+ str(row.id),
                                "name":row.name,
                                "complete_name":str(jsnp['name']) +' / ' + str(nietasT['name']) + ' / ' + str(nivel4['name']) + ' / '+ str(nivel5['name']) + ' / '+ str(nivel7['name']) +' / '+ str(row.name),
                                "categorias_Hijas":None
                            } for row in rows if row.parent_id == nivel7['id']]
                            
                            nietas[nivel7count]["categorias_Hijas"] = level7 if level7 is not None else 'sin hijas'
                            nivel7count = nivel7count+1
                        
                        nietas[nivel6count]["categorias_Hijas"] = level6 if level6 is not None else 'sin hijas'
                        nivel6count = nivel6count+1                    

                    level4[nivel5count]["categorias_Hijas"] = level5 if level5 is not None else 'sin hijas'
                    nivel5count = nivel5count+1
            

                nietas[nivel4count]["categorias_Hijas"] = level4 if level4 is not None else 'sin hijas'
                nivel4count = nivel4count+1
        except Exception as err:
            print(err)
        
        jsonhijas[qwe]["categorias_Hijas"] = nietas
        qwe = qwe+1

    jsonpadres[i]["categorias_Hijas"] = jsonhijas
    i = i+1    #así es 
print(dumps(jsonpadres))





# forNietas = 0
#         for nietasB in nietas:  
#             bisnietas = [{
#                 "id":row.id,
#                 "parent_path":row.parent_path,
#                 "name":row.name,
#                 "complete_name":row.complete_name,
#                 "categorias_Hijas":None
#             } for row in rows if row.parent_id == nietasB['id']]
            
#             nietas[forNietas]["categorias_Hijas"] = bisnietas
#             forNietas = forNietas+1




    # Creo que asi lo genera! pruebe a ver

    # if array is not None:
    #     categoryJson = [{
    #                 "id": categoria['id'],
    #                 "name": categoria['name'],
    #                 "picture": categoria['id'],
    #                 "total_items_in_this_category": None,
    #                 "path_from_root": [{
    #                             "id": path_root,
    #                             "name": complete_name
    #             }for path_root, complete_name in zip(categoria['parent_path'].split("/"),
    #                                                 categoria['complete_name'].split("/"))],
    #                 "children_categories": [{}],

    #                 "attribute_types": None,
    #                 "sexettings": {
    #                     "adult_content": False,
    #                     "buying_allowed": True
    #                 }
    #             }for categoria in array if categoria['parent_id'] is None]

    # print(dumps(categoryJson))

     








# {
#                                 "id": children_categories,
#                                 "name": complete_name_of_childrens
#                 }for children_categories, complete_name_of_childrens in zip(categoria['parent_path'].split("/"),
#                                                                             categoria['complete_name'].split("/")) 









# with conn:
#     sentencia = "select * from product_category"
#     cursor.execute(sentencia)
#     resultado = cursor.fetchall()
#     #   Se recorre los resultados y se guardan el un array
#     array = [] #    El array de retorno 
#     json = {        }
#     for row in resultado:            
#         json['id_Categoria'] = row.Categoria_id
#         json['nombre_Categoria'] = row.nombre_Categoria
#         json['level'] = row.level
#         json['imagen'] = row.imagen
#         array.append(json)
#         json = {}        
#     print(array)





