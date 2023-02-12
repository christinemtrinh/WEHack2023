from flask import Flask, render_template, redirect, url_for, flash, request
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse
import sqlite3

def get_db():
    db = sqlite3.connect('app.db')
    return db

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
	if request.method=="GET" and request.args.get('query')!=None:
		query = request.args.get('query')
		db = get_db()
		cursor = db.cursor()
		cursor.execute("SELECT * FROM Content WHERE topic LIKE ?", ('%'+query+'%',))
		topics = cursor.fetchall()
		if len(topics)==0:
			message="We don't have that information yet. Please try another topic!"
		else:
			message="Happy learnings!"
		return render_template('index.html', title='Home', topics=topics, query=query, message=message)
	science = ["bio", "cs", "ecs"]
	return render_template('index.html', title='Home', topic="")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/user/<username>')
@login_required
def user(username): 
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post 1'},
        {'author': user, 'body': 'Test post 2'}
    ]
    return render_template('user.html', user=user, posts=posts)