from flask import Flask
from config import Config
from views import * #linha de codigo para importa rotas
from models.pessoas import Cliente, Funcionario
from db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) #inicializando banco de dados

with app.app_context():
    db.create_all()
    
if __name__ == "__main__":
    app.run(debug = True)
    