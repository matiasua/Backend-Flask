from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS

# Se inicializa flask y retorna instancia llamada app
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost/pythonreactdb"
PyMongo(app)