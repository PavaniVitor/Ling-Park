from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post

@app.route('/')
def echo1():
    return 'ola mundo!'


@app.route('/cad')
def echo2():
    return render_template('cadastro.html')


@app.route('/echo1' , methods = ['POST' , 'GET'])
def echo3():
    nome = request.form['name']
    senha = request.form['password']
    placa_carro = request.form['car_plate']
    email = request.form['email']

    novo_usuario = User(nome , senha , placa_carro , email)
    db.session.add(novo_usuario)
    db.session.commit()
    #adicionar a logica de criação de usuario, impedir usuario duplicados etc
    return 'usuario criado com sucesso'