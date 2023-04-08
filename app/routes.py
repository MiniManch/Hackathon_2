from flask import render_template, url_for, request, redirect, flash
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user,current_user
from app.forms import add_user as login_form, search
from app import app, db
from app import models

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

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

@login_manager.user_loader
def load_user(user_id):
	return models.User.query.get(int(user_id))


@app.errorhandler(404)
def not_found(e):
	return f'Could not find {e}'


@app.route('/')
@app.route('/home')
def home():
	return render_template('index.html', pokemon=models.Pokemon.query.all())


@app.route('/all_pokemon',methods=['GET', 'POST'])
def pokemon():
	if current_user.is_authenticated:
		user = current_user
	else:
		user = None
	form = search()
	if form.is_submitted():
		data = dict(request.form)['search']
		return redirect(url_for('get_poke',poke_id_or_name = data))
	pokemon_to_show = models.Pokemon.query.all()

	return render_template('all_pokemon.html', pokemon=pokemon_to_show, types=types_list, form=form,user=user)


@app.route('/pokemon/<poke_id_or_name>')
def get_poke(poke_id_or_name):
	if current_user.is_authenticated:
		user = current_user
	else:
		user = None

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
	return render_template('get_poke.html', Pokemon=models.Pokemon.query.filter_by(id=poke_id).first(),user=user)


@app.route('/pokemon_by_type/<string:poke_type>', methods=['GET', 'POST'])
def by_type(poke_type):
	form = search()
	if form.is_submitted():
		data = dict(request.form)['search']
		return redirect(url_for('get_poke', poke_id_or_name=data))
	return render_template('all_pokemon.html', pokemon=models.Pokemon.query.filter_by(type=poke_type.lower()), types=types_list, form=form,user=current_user)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up_route():
	myForm = login_form()
	title = 'Sign up!'
	if myForm.is_submitted():
		this_user = models.User(id=request.form.get('id'),
		                        name=request.form.get('name'),
		                        password=request.form.get('password')
		                        # team=[]
		                        )
		actual_user = models.User.query.filter_by(name=this_user.name).first()
		if not actual_user:
			db.session.add(this_user)
			db.session.commit()
			flash(f'Welcome to the Pokemano world {request.form.get("name")}')
			return redirect(url_for('home'))
		else:
			flash('User already exists, try again')
			return redirect(url_for('sign_up_route'))
	return render_template('AddUser.html', form=myForm,title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
	myForm = login_form()
	title = 'Login!'
	if myForm.is_submitted():
		user = models.User.query.filter_by(name=request.form.get('name')).first()
		if user:
			if user.password == request.form.get('password'):
				login_user(user)
				flash(f'Logged in as {user.name}')
				return redirect(url_for('home'))
			else:
				flash(f'Wrong Password, try again')
		else:
			flash('User doesnt exist. try again')
	return render_template('AddUser.html', form=myForm,title=title)


@app.route('/add_to_team<int:pokemon_id>')
def add_to_team(pokemon_id):
	user = current_user
	this_pokemon = models.Pokemon.query.filter_by(id=pokemon_id).first()
	if len(user.team) < 3:
		user.team.append(this_pokemon)
		db.session.commit()
		flash(f'{this_pokemon.name} was added to your team!')
		print(user.team)
		return redirect(url_for('pokemon'))
	else:
		flash(f'{this_pokemon.name} cannot be added to your team! your team already has 3 pokemon in it.')
		return redirect(url_for('get_poke',poke_id_or_name = pokemon_id))


@app.route('/team')
@login_required
def team_route():
	return render_template('team.html',user=current_user )

