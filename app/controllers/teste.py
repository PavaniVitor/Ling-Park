from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post


#exemplo de arquivo de controller!

@app.route('/teste')
def echo_teste():
    print(logged_user)
    return 'ola denovo!'


@app.route('/users')
def echo_view_users():
#users recebe uma lista com todos os usuarios do banco de dados e ordena eles pelo username
    users = User.query.order_by(User.username).all()
    print(users[0].username)
    return render_template('users.html' , users = users)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/echo_login' , methods = ['POST' , 'GET'])
def login_echo():
    user_name = request.form['name']
    user_password = request.form['password']

    logged_user = User.query.filter_by(username = user_name).first()
    print(logged_user)
    if (logged_user != None):#checa se o usuario existe no banco de dados
        return 'eaeae   ' + str(logged_user.username) 
    else:
        return 'errrrrrrowwwwwwwwww' # vai pra pagina de erro no login


@app.route('/posts' , methods = ['POST' , 'GET'])
def posts():
    if request.method == 'POST':
        print('post')
        #posta a mensagem
    return 
    
    #mostra as mensagens do banco 
