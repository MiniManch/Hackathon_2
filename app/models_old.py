from app import db


class User(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    name         = db.Column(db.String(50), nullable=False)
    Win_record   = db.Column(db.String(50))
    current_team = db.relationship("Pokemon", backref="owner", lazy="dynamic")
    difficulty   = db.Column(db.String(50))

    def change_difficulty(self):
        if self.difficulty == 'easy':
            self.difficulty == 'hard'
        elif self.difficulty == 'hard':
            self.difficulty == 'easy'
        else:
            return False
        return f'your difficulty is now {self.difficulty}'

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


class Move_pokemon(db.Model):
    id         = db.Column(db.Integer, primary_key=True)
    move_id    = db.Column(db.Integer, db.ForeignKey('move.id'))
    pokemon_id = db.Column(db.Integer, db.ForeignKey('pokemon.id'))


class Move(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    acc         = db.Column(db.Integer, nullable=False)
    power       = db.Column(db.Integer, nullable=False)
    name        = db.Column(db.String(200), nullable=False)
    style       = db.Column(db.Boolean, default=True )
    effect_type = db.Column(db.String(50))
    type        = db.Column(db.String(50))

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)


class Pokemon(db.Model):
    id          =  db.Column(db.Integer, primary_key=True)
    name        =  db.Column(db.String(200), nullable=False)
    type        = db.Column(db.String(50), nullable=False)
    moves       = db.relationship('Move',secondary=Move_pokemon,backref='moves')
    strength    = db.Column(db.Integer, nullable=False,default=20)
    health      = db.Column(db.Integer, nullable=False,default=100)
    image_front = db.Column(db.String(200),nullable=False)
    image_back  = db.Column(db.String(200),nullable=False)
    owner_id    = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)
