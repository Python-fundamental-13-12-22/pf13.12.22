from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey
from sqlalchemy import String
import string
import secrets

from sqlalchemy.orm import backref

try:
    from local_settings import *
except:
    print("can't find local_settings")

def generate_password():
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    alphabet = letters + digits + special_chars
    pwd_length = 12
    while True:
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        if (any(char in special_chars for char in pwd) and
                sum(char in digits for char in pwd) >= 2):
            break
    return pwd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"{dialect}://{username}:{password}@{host}:{port}/{database}"
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(16), index=True)
    email = db.Column(String, index=True)
    password = db.Column(String(12), index=True)
    age = db.Column(Integer, index=True)
    def __init__(self, name, email, password,age):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
    def __repr__(self):
        return f"{self.id} {self.name} {self.email}  {self.age}"
    def __str__(self):
        return f"{self.id} {self.name} {self.email}  {self.age}"
    @classmethod
    def get_by_id(self,id):
        user = db.session.query(User).filter(User.id == id).first()
        return user
    @classmethod
    def get_all(cls):
        users = db.session.execute(db.select(User).order_by(User.id)).scalars()
        return users

    @classmethod
    def create(self,email, name, password, age):
        user = User(email, name, password, age)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete_user(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()
        return user


class Deck(db.Model):
    __tablename__ = "decks"
    id = db.Column(Integer, primary_key=True)
    name = db.Column(String(16), index=True)
    user_id = db.Column(Integer, ForeignKey('users.id'))
    user = db.relationship(User, backref=backref('decks', order_by=user_id))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id} {self.name} {self.user_id} "
    def __str__(self):
        return f"{self.id} {self.name} {self.user_id} "
    @classmethod
    def get_by_id(self,id):
        deck = db.session.query(Deck).filter(Deck.id == id).first()
        return deck
    @classmethod
    def get_all(cls):
        decks = db.session.execute(db.select(Deck).order_by(Deck.id)).scalars()
        return decks
    @classmethod
    def create(self, name, user_id):
        deck = Deck(name, user_id)
        db.session.add(deck)
        db.session.commit()
        return deck

class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('users.id'))
    user = db.relationship(User, backref=backref('cards', order_by=user_id))
    word = db.Column(String(16), index=True)
    translation = db.Column(String(16), index=True)
    tip = db.Column(String(16), index=True)

    def __init__(self,user_id, word, translation, tip):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    def __repr__(self):
        return f"{self.id} {self.word} {self.translation} {self.tip} "
    def __str__(self):
        return f"{self.id} {self.word} {self.translation} {self.tip} "
    @classmethod
    def get_by_id(self,id):
        card = db.session.query(Card).filter(Card.id == id).first()
        return card
    @classmethod
    def get_all(cls):
        card = db.session.execute(db.select(Card).order_by(Card.id)).scalars()
        return card

    @classmethod
    def create(self,user_id, word,translation,tip):
        card = Card(user_id,word,translation,tip)
        db.session.add(card)
        db.session.commit()
        return card
@app.route("/")
def home():
    return render_template('home.html')
@app.route("/user")
def user():
    user_list = User.get_all()
    return render_template('user/user_list.html', users=user_list, title="User list")
@app.route("/user/<user_id>")
def get_user_id(user_id):
    user = User.get_by_id(user_id)
    if user:
        result = render_template('user/user_info.html', user=user, title="User info")
    else:
        result = render_template('user/user_404.html')
    return result

@app.route('/user/create', methods=["POST", "GET"])
def user_create():
    if request.method == "GET":
        return render_template('user/user_create.html', title="User create")
    if request.method == "POST":
        email = request.form["email"]
        name = request.form["name"]
        age = request.form["age"]
        password = generate_password()
        user = User.create(name,email,password,age)
        return redirect(url_for("get_user_id", user_id=user.id))

@app.route('/user/delete/<user_id>')
def user_delete(user_id):
    user = User.delete_user(user_id)
    if user:
        user_list = User.get_all()
        result = render_template('user/user_list.html',users=user_list)
    else:
        result = render_template('user/user_404.html', title="User 404")
    return result
@app.route("/deck")
def deck():
    deck_list = Deck.get_all()
    return render_template('deck/deck_list.html', decks=deck_list, title="Deck list")
@app.route("/deck/<deck_id>")
def get_deck_by_id(deck_id):
    deck = Deck.get_by_id(deck_id)
    if deck:
        result = render_template('deck/deck_info.html', deck=deck, title="Deck info")
    else:
        result = render_template('deck/deck_404.html', title="Deck 404")
    return result
@app.route('/deck/create', methods=["POST", "GET"])
def deck_create():
    if request.method == "GET":
        users = User.get_all()
        return render_template('deck/deck_create.html', title="Deck create", users = users)
    if request.method == "POST":
        name = request.form["name"]
        user_id = request.form["user_id"]
        deck = Deck.create(name,user_id)
        return redirect(url_for("get_deck_by_id", deck_id=deck.id))

@app.route("/card")
def card():
    card_list = Card.get_all()
    return render_template('card/card_list.html', cards=card_list, title="Card list")

@app.route("/card/<card_id>")
def get_card_by_id(card_id):
    card = Card.get_by_id(card_id)
    if card:
        result = render_template('card/card_info.html', card=card, title="Card info")
    else:
        result = render_template('card/card_404.html', title="Card 404")
    return result

@app.route('/card/create', methods=["POST", "GET"])
def card_create():
    if request.method == "GET":
        users = User.get_all()
        return render_template('card/card_create.html', title="Card create", users=users)
    if request.method == "POST":
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        user_id = request.form["user_id"]
        card = Card.create(user_id,word,translation,tip)
        return redirect(url_for("get_card_by_id", card_id=card.id))




if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run()

