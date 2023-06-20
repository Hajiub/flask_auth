from flask import Blueprint, render_template, request
from .models import User
from .forms import LoginFrom, SigninForm


auth = Blueprint('auth', __name__)

@auth.route('/signin',methods=['POST', 'GET'])
def signin_view():
    form = SigninForm()
    if form.validate_on_submit():
        return form.data
    return render_template('auth/signin.html', form=form)


@auth.route('/login')
def login_view():
    return render_template('auth/login.html')


@auth.route('/logout')
def logout_fun():
    pass