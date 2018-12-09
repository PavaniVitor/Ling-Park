from flask import render_template, request, redirect, url_for, flash
from app import app, login_manager
from app import db
from app.models.tables import User, Post, Mention
from app.models.forms import PostForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/home', methods=['POST', 'GET'])
@login_required
def home():
    lista_posts = Post.query.order_by(Post.id).all()
    lista_posts.reverse()
    n = 0
    if len(lista_posts) > 20:
        n = 20
    else:
        n = len(lista_posts)
    user = current_user
    # adicionar logica para buscar os usuarios que fizeram o post no banco

    form = PostForm(request.form)
    return render_template('home.html', posts=lista_posts, form=form, num=n)


@app.route('/echo', methods=['POST', 'GET'])
def echo_post():
    form = PostForm(request.form)
    user = current_user
    if request.method == 'POST':
        post = Post(form.content.data, user.id, form.matter_field.data)
        db.session.add(post)
        db.session.flush()
        db.session.refresh(post)
        mention_plate(form.content.data, post.id)
        db.session.commit()

    return(redirect(url_for('home')))


def mention_plate(message, id_post):
    c = '@'
    pos = [pos for pos, char in enumerate(message) if char == c]
    if not pos:
        return

    else:
        for p in pos:
            plate = message[p+1:p+8]
            print(plate)

            # ate aqui funciona

            for i in range(3):
                if plate[i].isdigit():
                    continue
            if not plate[3].isdigit():
                continue
            if not plate[4].isdigit():
                if not plate[4].isalpha():
                    continue
            if not plate[5].isdigit():
                continue
            if not plate[6].isdigit():
                continue
            
            car_owner = User.query.filter_by(car_plate=plate).all()
            for car in car_owner:
                mention = Mention(car.id, id_post)
                db.session.add(mention)
