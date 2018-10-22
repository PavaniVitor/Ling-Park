from flask import render_template, request, flash, redirect
from flask_login import login_user, logout_user
from app import app
from app import db
from app import login_manager
from app.models.tables import User, Post
from app.models.forms import login_form

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(alternative_id=user_id).first()

@app.route('/')
def echo1():
    return render_template('home.html')


@app.route("/login" , methods=['GET', 'POST'])                
def login():                                                    
    form = login_form() 
    if form.validate_on_submit():                            
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash("Login efetuado com sucesso")            #tem que pegar essa função flash na documentação
            return redirect(url_for('index'))                              #e colocar na base.html
                                                         
        else:                                          
            flash("Ops! Ocorreu algum erro. Tente novamente.")                                
    return render_template('login.html' , form_login=form)


@app.route("/logout")
def logout():
    logout_user()
    flash("Obrigado por utilizar nossos servicos. Volte sempre")
    return redirect(url_for('index'))


@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Parabens!Voce esta registrado no Estaciona-CT')
        return redirect(url_for('login'))
    return render_template('cadastro.html', title='Cadastro', form_register=form)


#@app.route("/teste/<info>")
#@app.route("teste" , defaults={"info": None})
#def teste():
#    x
#    db.session.add(x)
#    db.session.commit()
