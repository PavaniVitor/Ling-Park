from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
app.config.from_object('config.py')
db = SQLAlchemy(app)
from app.models import tables
migrate = Migrate(app,db)


manager = Manager(app)
manager.add_command('db' , MigrateCommand)

from app.controllers import default