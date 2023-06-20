from flask import Blueprint, render_template, request, flash , redirect, url_for
from flask_login import login_user
from .models import User
from .forms import LoginFrom, SigninForm
from werkzeug.security import check_password_hash, generate_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/signin',methods=['POST', 'GET'])
def signin_view():
    form = SigninForm()
    if form.validate_on_submit():
        user  = User(
            username = form.data.get('username'),
            email    = form.data.get('email'),
            hashed_password = generate_password_hash(form.data.get('password1'), method="pbkdf2:sha256")

        )
        try:
            db.session.add(user)
            login_user(user, remember=True)
            return redirect(url_for('auth.login'))
        except Exception as e:
            flash('An error accured! {0}'.format(e))
            return redirect(url_for('auth.signin_view'))
        
        
    return render_template('auth/signin.html', form=form)


@auth.route('/login')
def login_view():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout_fun():
    pass