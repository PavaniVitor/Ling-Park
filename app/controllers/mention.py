from flask import render_template, request, redirect, url_for, flash
from app import app, login_manager
from app import db
from app.models.tables import User, Post, Mention
from app.models.forms import PostForm
from flask_login import login_user, current_user, logout_user, login_required


@app.route('/notification', methods=['POST', 'GET'])
@login_required
def mentions():
    user = current_user
    print(current_user.id)
    _mentions = Mention.query.filter_by(mentioned_id = current_user.id)

    lista_posts = []
    for i in range(_mentions.count()):
        lista_posts.append(_mentions[i].post)
    
    num = len(lista_posts)
    return render_template('notification.html', posts=lista_posts , num = num)
