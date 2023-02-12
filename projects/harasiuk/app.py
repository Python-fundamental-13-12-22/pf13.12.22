from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

dialect = "postgresql"
username = "postgres"
password = "root"
host = "localhost"
port = "5432"
database = "project"
try:
    from local_settings import *
except:
    print("can't find local_settings")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = f"{dialect}://{username}:{password}@{host}:{port}/{database}"
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String)
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<{self.id}. {self.name}>"


class Deck(db.Model):
    __tablename__ = "decks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"<{self.id}. {self.name}>"


class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    word = db.Column(db.String)
    translation = db.Column(db.String)
    tip = db.Column(db.String)

    def __init__(self, user_id, word, tip, translation):
        self.user_id = user_id
        self.word = word
        self.tip = tip
        self.translation = translation

    def __repr__(self):
        return f"<{self.id}. {self.word}>"


def deck_create(name, user_id):
    deck = Deck(name=name, user_id=user_id)
    db.session.add(deck)
    db.session.commit()
    return deck


def deck_get_by_id(deck_id):
    deck = db.session.get(Deck, deck_id)
    return deck


def deck_update(deck_id, name):
    deck = db.session.get(Deck, deck_id)
    deck.name = name
    db.session.add(deck)
    db.session.commit()
    return deck


def deck_delete_by_id(deck_id):
    deck = db.session.get(Deck, deck_id)
    if deck:
        db.session.delete(deck)
        db.session.commit()
        return True
    else:
        return False


def card_create(user_id, word, translation, tip):
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    db.session.add(card)
    db.session.commit()
    return card


def card_get_by_id(card_id):
    card = db.session.get(Card, card_id)
    return card


def card_update(card_id, word=None, translation=None, tip=None):
    card = db.session.get(Card, card_id)
    card.word = word
    card.translation = translation
    card.tip = tip
    db.session.add(card)
    db.session.commit()
    return card


def card_delete_by_id(card_id):
    card = db.session.get(Card, card_id)
    if card:
        db.session.delete(card)
        db.session.commit()
        return True
    else:
        return False


def card_filter(sub_word):
    cards = tuple(db.session.query(Card).filter(or_(
        Card.word.ilike(f"%{sub_word}%"),
        Card.tip.ilike(f"%{sub_word}%"),
        Card.translation.ilike(f"%{sub_word}%")
    )).all())
    return cards


def user_create(name, email, password):
    user = User(name=name, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    return


def user_get_by_id(user_id):
    user = db.session.get(User, user_id)
    return user


def user_update_name(user_id, name):
    user = db.session.get(User, user_id)
    user.name = name
    db.session.add(user)
    db.session.commit()


def user_change_password(user_id, old_password, new_password):
    user = db.session.get(User, user_id)
    if old_password == user.password and user:
        user.password = new_password
        db.session.add(user)
        db.session.commit()
        return True
    else:
        return False


def user_delete_by_id(user_id):
    user = db.session.get(User, user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    else:
        return False

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
