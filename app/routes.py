from flask import render_template, flash, redirect, url_for

from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Andrey'}

    posts = [
        {
            'author': {'username' : 'Max'},
            'body': 'Hi, nice day, isnt it?'
        },
        {
            'author': {'username' : 'Susan'},
            'body' : 'Fantastic job'
        },
        {
            'author': {'username' : 'Nick'},
            'body': 'Waiting for you answer'
        }
    ]

    return render_template('index.html', 
                            title = 'Home Page', 
                            user = user, 
                            posts = posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))

    return render_template('login.html',
                            title = 'Sign in',
                            form = form)

@app.route('/test')
def test():
    return render_template('test.html',title = 'Test')