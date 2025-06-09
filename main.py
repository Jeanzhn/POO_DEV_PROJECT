from flask import Flask

app = Flask(__name__)

#linha de codigo para importa rotas
from views import *

if __name__ == "__main__":
    app.run(debug = True)
    