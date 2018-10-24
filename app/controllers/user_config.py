from flask import render_template, request , redirect , url_for
from app import app
from app import db
from app.models.tables import User, Post
from flask_login import login_required , current_user , login_manager

@app.route('/config')
@login_required
def config():

    user = current_user
    return render_template('preferences.html' , user = user )
