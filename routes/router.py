#Modulos relacionados con flask
from flask import Flask, render_template, request, Response
from flask_bootstrap import Bootstrap
from flask_restful import Resource, Api,reqparse
from flask_cors import CORS
import os
#Clases modulos
template_dir = os.path.abspath('public')
app = Flask(__name__, template_folder=template_dir)
#Configuraciones iniciales
Bootstrap(app)
api = Api(app)
resource = Resource
req = request
response = Response
reqpar = reqparse
cors = CORS(app, resources={r"/*": {"origins": "*","headers":"X-Custom-Header"}})

#Importando todas las clases de rutas y aniadendolas
from routes.add_route.rcategorias import get_categorias
from routes.add_route.Rproduct import Rproduct
from routes.add_route.RplanesCategory import RplanesCategory

#       ----    RUTAS DEL PROYECTO  ----        #
#add-rutas

api.add_resource(get_categorias,'/Categorias')
api.add_resource(Rproduct,'/router_product', methods=['GET', 'POST', 'DELETE', 'PUT'])
api.add_resource(RplanesCategory,'/router_planesCategory', methods=['GET']) 
#       ----    FIN DE LAS RUTAS PROYECTO  ----        #

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return '¿que estas buscando? :)'
    else:
        return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    if request.method == 'POST':
        return 'Error'
    else:
        return render_template("error.html"), 404
