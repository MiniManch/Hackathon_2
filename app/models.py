from app import db


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	team = db.relationship('Pokemon', backref='owner')
	password = db.Column(db.String(50), nullable=False)


move_pokemon_table = db.Table(
	'PokemonMove',
	db.Column('move_id',db.Integer, db.ForeignKey('move.id')),
	db.Column('pokemon_id',db.Integer, db.ForeignKey('pokemon.id'))
)


class Move(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	acc = db.Column(db.Integer, nullable=False)
	power = db.Column(db.Integer, nullable=False)
	name = db.Column(db.String(200), nullable=False)
	effect_type = db.Column(db.String(50))
	effect_power = db.Column(db.Integer)
	type = db.Column(db.String(50))

	def __init__(self, dictionary):
		for key, value in dictionary.items():
			setattr(self, key, value)


class Pokemon(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(50), nullable=False)
	health = db.Column(db.Integer, default=100)
	attack = db.Column(db.Integer, default=100)
	owner_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	moves = db.relationship('Move', secondary=move_pokemon_table, backref='pokemon')
	type = db.Column(db.String(50),nullable=False)
	image_front = db.Column(db.String(200), nullable=False)
	image_back = db.Column(db.String(200), nullable=False)

	def __init__(self, dictionary):
		for key, value in dictionary.items():
			setattr(self, key, value)