from app import db


class User(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(50), nullable=False)
    Win_record   = db.Column(db.String(50), nullable=False)
    fave_poke    = db.Column(db.Integer, db.ForeignKey("pokemon.id"))
    current_team = db.relationship("Pokemon", backref="current_owner", lazy="dynamic")
    difficulty   = db.Column(db.String(50))

    def change_difficulty(self):
        if self.difficulty == 'easy':
            self.difficulty == 'hard'
        elif self.difficulty == 'hard':
            self.difficulty == 'easy'
        else:
            return False
        return f'your difficulty is now {self.difficulty}'

class Move_pokemon:
    move_id = db.Column(db.Integer,db.ForeignKey('move.id'))
    pokemon_id = db.Column(db.Integer,db.ForeignKey('pokemon.id'))

class Move(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    acc         = db.Column(db.Integer, nullable=False)
    power       = db.Column(db.Integer, nullable=False)
    name        = db.Column(db.String(200), nullable=False)
    style       = db.Column(db.Boolean, default=True )
    effect_type = db.Column(db.String(50), default='Attack')
    type        = db.Column(db.String(50))


class Pokemon(db.Model):
    id       =  db.Column(db.Integer, primary_key=True)
    name     =  db.Column(db.String(200), nullable=False)
    type     = db.Column(db.String(50), nullable=False)
    moves    = db.relationship('Move',secondary=Move_pokemon,backref='moves')
    strength = db.Column(db.Integer, nullable=False,default=20)
    health   = db.Column(db.Integer, nullable=False,default=100)
    owner    = db.Column(db.Integer,db.ForeignKey('user.id'))
