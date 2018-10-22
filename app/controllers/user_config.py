from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post
from flask_login import login_required

@login_required
@app.route('/config')
def config():
    return render_template('config.html')