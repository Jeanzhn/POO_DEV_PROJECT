from flask import Flask
from flask_migrate import Migrate
from config import Config
from models.pessoas import Cliente, Funcionario
from models.crud import CRUD
from db import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app) #inicializando banco de dados
migrate = Migrate(app , db)

from views import * #importando rotas

if __name__ == "__main__":
    with app.app_context(): #criando banco de dados se não existir
        db.create_all()
    app.run(debug = True)
    