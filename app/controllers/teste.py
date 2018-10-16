from flask import render_template, request
from app import app
from app import db
from app.models.tables import User, Post

#exemplo de arquivo de controller!

@app.route('/teste')
def echo_teste():
    return 'ola denovo!'