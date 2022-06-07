from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.controllers import cadastro
from app.controllers import atualizacao
from app.controllers import consulta
from app.controllers import delecao






