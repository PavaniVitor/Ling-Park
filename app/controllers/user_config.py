from flask import render_template, request , redirect , url_for , flash
from app import app
from app import db
from app.models.tables import User, Post
from flask_login import login_required , current_user , login_manager
from sqlalchemy import update
from app.models.forms import PreferencesForm
from werkzeug.security import generate_password_hash , check_password_hash

@app.route('/preferences' , methods = ['GET' , 'POST'])
@login_required
def config_password():
    user = current_user
    form = PreferencesForm(request.form)

    user_db = User.query.filter_by(id = user.id).first()
    if request.method == 'POST':
        if user.check_password(form.password.data):
            #do
            if form.car_plate.data != '':
                user_db.car_plate = form.car_plate.data
            if form.car_plate2.data != '':
                user_db.car_plate2 = form.car_plate2.data
            db.session.commit()
                

    return render_template('preferences.html' , user = user , form=form)
