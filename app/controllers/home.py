from flask import render_template, url_for, flash
from app import app, db
from app.models.tables import Post
from flask_login import login_required , current_user
from app.models.forms import PostForm


@app.route('/home', methods = ['POST' , 'GET'])
@login_required
def home():
    lista_posts = Post.query.order_by(Post.id).all()
    lista_posts.reverse()
    lista_posts = lista_posts[:20 - len(lista_posts)]
    user = current_user
    form = Post()
    if form.is_authenticated():
        #publica o post
        post = Post(form.text.data, user.id)
        db.session.add(post)
        db.session.commit()
        flash('Mensagem publicada com sucesso')
    return render_template('home.html' , posts=lista_posts)


    