from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post

#exemplo de arquivo de controller!

@app.route('/teste')
def echo_teste():
    return 'ola denovo!'

@app.route('/users')
def echo_view_users():
#users recebe uma lista com todos os usuarios do banco de dados e ordena eles pelo username
    users = User.query.order_by(User.username).all()
    print(users[0].username)
    return render_template('users.html' , users = users)