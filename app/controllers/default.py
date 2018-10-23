from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post

@app.route('/')
def echo1():
    return render_template('index.html')  #Esse html deve ter o botão pra login e o botão pra cadastro
