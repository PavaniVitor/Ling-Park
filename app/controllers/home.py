from flask import render_template, request, redirect, url_for , flash
from app import app, login_manager
from app import db
from app.models.tables import User, Post
from app.models.forms import PostForm
from flask_login import login_user , current_user , logout_user , login_required

@app.route('/home', methods = ['POST' , 'GET'])
@login_required
def home():
    lista_posts = Post.query.order_by(Post.id).all()
    lista_posts.reverse()
    n = 0
    if len(lista_posts) > 20 :
        n = 20
    else:
        n = len(lista_posts)
    user = current_user
    #adicionar logica para buscar os usuarios que fizeram o post no banco

    form = PostForm(request.form)
    return render_template('home.html' , posts=lista_posts, form = form, num = n)

@app.route('/echo', methods=['POST', 'GET'])
def echo_post():
    form = PostForm(request.form)
    user=current_user
    if request.method == 'POST' :
        print('alou')
        #publica o post
        post = Post(form.content.data, user.id)
        db.session.add(post)
        db.session.commit()
    return(redirect(url_for('home')))

