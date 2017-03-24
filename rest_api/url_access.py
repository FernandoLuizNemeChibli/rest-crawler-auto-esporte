from .forms import RegisterForm
from .models import User
from flask import abort
from flask import jsonify
from flask import request
from flask import render_template
from page_crawler import get_information
from page_crawler import load_information
from rest_api import flask_application
from rest_api import db
from flask import make_response
from flask import redirect
from werkzeug.security import generate_password_hash, check_password_hash

@flask_application.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
    
@flask_application.route('/restapi/<from_where>', methods=['GET','POST'])
def restapi(from_where):
	if from_where!="fromsite" and from_where!="fromfile":
		abort(400)
	if not request.json or not 'nickname' in request.json or not 'password' in request.json:
		abort(400)
	entered_user=User.query.filter_by(nickname=request.json["nickname"]).first()
	if entered_user is None:
		abort(400)
	if not check_password_hash(entered_user.password,request.json["password"]):
		abort(400)
	return jsonify(get_information() if from_where=="fromsite" else load_information())
	
@flask_application.route('/register',methods=['GET','POST'])
def register():
	form=RegisterForm()
	if form.validate_on_submit():
		new_user=User(
			nickname=form.nickname.data,
			email=form.email.data,
			password=generate_password_hash(form.password.data)
		)
		db.session.add(new_user)
		db.session.commit()
		flash("User registred! Please log in to continue to your new account!")
		return redirect(url_for('login'))
	return render_template('register.html',title='Registro',form=form)
	
@flask_application.route('/',methods=['GET','POST'])
def index():
	return render_template('index.html')
