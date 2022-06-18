from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)


app.config.from_object('config')
db = SQLAlchemy(app)






from app.controllers import cadastro
from app.controllers import consulta
from app.controllers import login
from app.controllers import inicial
from app.controllers import detalhes






