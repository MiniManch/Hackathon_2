from flask import render_template, url_for, request, redirect, flash
from app.forms import add_user as login_form
from app import app, db
from app import models


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', pokemon=models.Pokemon.query.all())


@app.route('/all_pokemon')
def pokemon():
	return render_template('all_pokemon.html', pokemon=models.Pokemon.query.all())


@app.route('/pokemon/<int:poke_id>')
def get_poke(poke_id):
	return render_template('get_poke.html', pet=models.Pokemon.query.filter_by(id=poke_id).first())


# @app.route('/team/<int:user_id>')
# def team(user_id):
# 	if not user_id:
# 		user_id = 0
# 	return render_template('index.html', user_id=user_id)


# @app.route('/add_to_cart/<int:pet_id>/<int:cart_id>')
# def add_to_cart(pet_id, cart_id):
# 	my_cart = models.Cart.query.filter_by(id=1).first()
# 	my_cart.add_to_cart(pet_id)
# 	return redirect(url_for('pets'))
#

@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up_route():
	myForm = login_form()
	if myForm.is_submitted():
		this_user = models.User(id=request.form.get('id'),
		                        name=request.form.get('name'),
		                        passsword=request.form.get('password'),
		                        team=[]
		                        )
		db.session.add(this_user)
		db.session.commit()
		flash(f'Welcome to the Pokemon world {request.form.get("name")}')
		return redirect(url_for('home'))
	return render_template('AddUser.html', form=myForm)
#
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
# 	myForm = login_form()
# 	if myForm.is_submitted():
# 		this_user = dict(request.form)
# 		users  = User.query.all()
# 		for user in users:
# 			if this_user['name']  == user.name and this_user['city'] == user.city:
# 				flash(f'You are now logged in {this_user["name"]}', "success")
# 				return redirect(url_for('home'))
# 		flash('user not found')
# 	return render_template('login.html', form=myForm)
