from flask import Blueprint, render_template, redirect, url_for, flash
from strike_app import db
from strike_app.auth.models import User
from strike_app.auth.forms import LoginForm
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash

auth_blueprint = Blueprint('auth', __name__, template_folder='templates')

### Routes

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    feedback = None

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('staking.strikers'))
        else:
            feedback = "Foutieve login."

    return render_template("login.html", form=login_form, feedback=feedback)

@auth_blueprint.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Je bent nu uitgelogd.")
    return redirect(url_for('index'))