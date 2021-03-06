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
login_manager.login_view = 'login'

from app.controllers import default
from app.controllers import log_reg
from app.controllers import home
from app.controllers import user_config
from app.controllers import mention
