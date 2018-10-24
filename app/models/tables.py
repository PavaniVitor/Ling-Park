from app import db
from werkzeug.security import generate_password_hash , check_password_hash
from datetime import datetime


class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer , primary_key=True)
    username = db.Column(db.String , unique = True)
    password = db.Column(db.String)
    car_plate = db.Column(db.String)
    email = db.Column(db.String , unique = True)

    @property 
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True
    
    @property
    def is_anonymous(self):
        return True
    
    def get_id(self):
        return str(self.id)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self , password):
        return check_password_hash(self.password, password)


    def __init__ (self, username, password , car_plate , email):
        self.username = username
        self.password = generate_password_hash(password)
        self.car_plate = car_plate
        self.email = email
    
    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer , primary_key = True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer , db.ForeignKey('users.id'))
    owner = db.relationship('User' , foreign_keys = user_id)
    date = db.Column(db.DateTime, nullable=False)

    def __init__(self, content , user_id):
        self.content = content
        self.user_id = user_id
        self.date = datetime.utcnow

    def __repr__(self):
        return '<Post %r>' % self.id
 
