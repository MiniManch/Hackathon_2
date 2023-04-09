from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from app.my_functions import get_random_string, populate_pokemon, populate_moves
from app import create_db

app = Flask(__name__)
#
# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/hackathon_2?charset=utf8mb4'

# Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
# app.config['DEBUG'] = True

# Initialize The Database
db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)
#
from app import models
from app import routes

pokemon_file = 'app/static/pokemon.json'
moves_file = 'app/static/final_moves.json'

# with app.app_context():
# 	pass
	# db.drop_all()
	# db.create_all()
	# populate_moves(database=db, model=models.Move, json_file=moves_file)
	# populate_pokemon(database=db, model=models.Pokemon, model_2=models.Move, json_file=pokemon_file)
	# db.session.commit()





