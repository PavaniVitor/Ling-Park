from flask import render_template, url_for, flash
from app import app, db
from app.models.tables import Post


@app.route('/home')
def home():
    lista_posts = Post.query.order_by(Post.id).all()
    lista_posts.reverse()
    lista_posts = lista_posts[:20 - len(lista_posts)]
    return render_template('home.html' , posts=lista_posts)

def postar():
    
    return render_template() 
    