from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from app.models import tables
migrate = Migrate(app,db)


manager = Manager(app)
manager.add_command('db' , MigrateCommand)

login_manager = LoginManager(app)

#importe aqui os controllers para as paginas
from app.controllers import default
from app.controllers import teste
