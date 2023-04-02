from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import flask_migrate
from app.my_functions import get_random_string,populate_database
# from app import create_db

app = Flask(__name__)

# configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:admatainov14!@localhost/hackathon_2?charset=utf8mb4'

# Secret Key
app.config['SECRET_KEY'] = get_random_string(256)
app.config['DEBUG'] = True

# Initialize The Database 
db = SQLAlchemy(app)
migrate = flask_migrate.Migrate(app, db)

from app import models
from app import routes

my_file = 'app/static/users.json'

with app.app_context():
	for pet in models.Pet.query.all():
		db.session.delete(pet)
	db.session.commit()
	db.drop_all()
	db.create_all()
	populate_database(db,models.Pet,my_file)
	my_cart = models.Cart(id = 1)
	db.session.add(my_cart)
	db.session.commit()


