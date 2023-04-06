from flask import render_template, url_for, request, redirect, flash
from app.forms import add_user as login_form
from app import app, db
from app import models

types_list = [
	'Electric',
	'Grass' ,
	'Rock',
	'Flying',
	'Normal',
	'Psychic',
	'Fighting',
	'Water',
	'Fire',
	'Ghost',
	'Ground'
]


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', pokemon=models.Pokemon.query.all())


@app.route('/all_pokemon')
def pokemon():
	pokemon_to_show = models.Pokemon.query.all()
	return render_template('all_pokemon.html', pokemon=pokemon_to_show, types=types_list)


@app.route('/pokemon/<poke_id_or_name>')
def get_poke(poke_id_or_name):
	if poke_id_or_name.isnumeric():
		try:
			poke_id = models.Pokemon.query.filter_by(id=poke_id_or_name).first().id
		except:
			return not_found(poke_id_or_name)
	elif poke_id_or_name.isalpha():
		try:
			print('a')
			poke_id = models.Pokemon.query.filter_by(name=poke_id_or_name.lower()).first().id
		except:
			return not_found(poke_id_or_name)
	return render_template('get_poke.html', Pokemon=models.Pokemon.query.filter_by(id=poke_id).first())


@app.route('/pokemon_by_type/<string:poke_type>')
def by_type(poke_type):
	print(models.Pokemon.query.filter_by(type=poke_type.lower()))
	return render_template('all_pokemon.html', pokemon=models.Pokemon.query.filter_by(type=poke_type.lower()), types=types_list)


@app.errorhandler(404)
def not_found(e):
	return f'Could not find {e}'

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
		                        password=request.form.get('password'),
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
