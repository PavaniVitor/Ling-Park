from flask import render_template, request , redirect , url_for
from app import app
from app import db
from app.models.tables import User, Post
from flask_login import login_required , current_user , login_manager
from sqlalchemy import update
from app.models.forms import NewPasswordForm , validate_car_plate

@app.route('/config')
@login_required
def config_password():
    user = current_user
    newpassword = NewPasswordForm
    new_password = update(user).where(user.password).values(newpassword)  
    return render_template('preferences.html' , user = user )

def config_newplate():
    user = current_user
    newcar_plate    # recebe a variavel do html
    validate_car_plate(self, newcar_plate): 
    if user.car_plate2 is None:
        car_plate2 = update(user).where(user.car_plate2).values(newcar_plate)
    else:
        if user.car_plate3 is None:
            car_plate3 = update(user).where(user.car_plate3).values(newcar_plate)
        else:
            car_plate2 = update(user).where(user.car_plate2).values(newcar_plate)
    return render_template('preferences.html' , user = user )