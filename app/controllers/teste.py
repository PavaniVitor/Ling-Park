from flask import render_template, request, redirect, url_for , flash
from app import app, login_manager
from app import db
from app.models.tables import User, Post
from app.models.forms import LoginForm
from flask_login import login_user , current_user , logout_user


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/users')
def echo_view_users():
#users recebe uma lista com todos os usuarios do banco de dados e ordena eles pelo username
    users = User.query.order_by(User.username).all()
    print(users[0].username)
    return render_template('users.html' , users = users)

@app.route('/login' , methods = ['POST' , 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('echo_logado'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('echo_logado'))
        print(form.username.data)
        print(form.password.data)
        print(form.remember_me.data)
    return render_template('login.html', login_form = form)

@app.route('/logado')
def echo_logado():
    print(current_user.is_authenticated)
    print(current_user)
    if current_user.is_authenticated:
        return 'você esta logado!'
    else:
        return 'você não esta logado!'

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))   #   para usar essa função, chame o metodo que esta 
                                        #   decorando a rota que vc deseja mandar o usuario
