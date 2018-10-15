from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)
<<<<<<< HEAD
app.config.from_object('config')
=======
app.config.from_object('config.py')
>>>>>>> 4074ca40b11a7ef0040afd1a74a4819efc66b351
db = SQLAlchemy(app)
from app.models import tables
migrate = Migrate(app,db)


manager = Manager(app)
manager.add_command('db' , MigrateCommand)

from app.controllers import default