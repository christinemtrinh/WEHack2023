from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Miguel'}
	science = ["bio", "cs", "ecs"]
	return render_template('index.html', title='Home', user=user, science=science)

@app.route('/login', methods=['GET', 'POST'])
def login(): 
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for user {}, remember_me={}'.format(
			form.uname.data, form.remember_me.data))
		return redirect(url_for('index'))
	return render_template('login.html', title='Sign In', form=form)
