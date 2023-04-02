from app import db


class Cart(db.Model):
    id   = db.Column(db.Integer, primary_key=True)
    pets = db.relationship("Pet", backref="my_cart", lazy="dynamic")

    def add_to_cart(self,pet_id):
        pet = Pet.query.filter_by(id=pet_id).first()
        pet.cart = self.id
        db.session.commit()

    def get_total(self):
        total = 0
        for pet in self.pets:
            total += pet.price
        db.session.commit()

    @classmethod
    def get_cart(cls):
        return cls.query.all()


class Pet(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(50), nullable=False)
    gender      = db.Column(db.String(50), nullable=False)
    breed       = db.Column(db.String(50), nullable=False)
    birth_date  = db.Column(db.Date(), nullable=False)
    details     = db.Column(db.String(200), nullable=False)
    price       = db.Column(db.Integer, nullable=False)
    image       = db.Column(db.String(200), nullable=False)
    cart        = db.Column(db.Integer, db.ForeignKey("cart.id"))


