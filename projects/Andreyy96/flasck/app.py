from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template

dialect = "-----------"
username = "---------"
password = "----"
host = "---------"
port = "----"
database = "-------"

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
    username = db.Column(db.String)
    password = db.Column(db.Integer)

    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password

    def __repr__(self):
        return f"{self.id} {self.email}"

    def __str__(self):
        return f"{self.id} {self.email} {self.username} {self.password}"

    @classmethod
    def get_by_id(cls, id):
        user = db.session.query(User).filter(User.id == id).first()
        return user

    @classmethod
    def get_all(cls):
        users = db.session.execute(db.select(User).order_by(User.username)).scalars()
        return users

    @classmethod
    def create_user(cls, email, username, password):
        user = User(email, username, password)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('no_find_id.html')
        return self


class Deck(db.Model):
    __tablename__ = "decks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('decks.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id}, {self.name}'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.user_id}'

    @classmethod
    def get_by_id(cls, id):
        deck = db.session.query(Deck).filter(Deck.id == id).first()
        return deck

    @classmethod
    def get_all_deck_user_id(cls, user_id):
        deck = db.session.query(Deck).filter(Deck.user_id == user_id).all()
        return deck

    @classmethod
    def get_all(cls):
        decks = db.session.execute(db.select(Deck).order_by(Deck.name)).scalars()
        return decks

    @classmethod
    def create_deck(cls, name, user_id):
        deck = Deck(name, user_id)
        db.session.add(deck)
        db.session.commit()
        return deck

    def update(self, name, user_id):
        self.name = name
        self.user_id = user_id
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('no_find_id.html')
        return self


class Card(db.Model):
    __tablename__ = "cards"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    word = db.Column(db.String)
    translation = db.Column(db.String)
    tip = db.Column(db.String)

    def __init__(self, user_id, word, translation, tip):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    def __str__(self):
        return f'{self.id}, {self.user_id=}, {self.word},  {self.translation}, {self.tip}'

    def __repr__(self):
        return f'{self.id}, {self.word},  {self.translation}, {self.tip}'

    @classmethod
    def get_by_id(cls, id):
        card = db.session.query(Card).filter(Card.id == id).first()
        return card

    @classmethod
    def get_all_card_user_id(cls, user_id):
        cards = db.session.query(Card).filter(Card.user_id == user_id).all()
        return cards

    @classmethod
    def get_all(cls):
        cards = db.session.execute(db.select(Card).order_by(Card.word)).scalars()
        return cards

    @classmethod
    def card_filter(cls, sub_word):
        cards = tuple(db.session.query(Card).filter
                      (Card.word == sub_word or Card.translation == sub_word or Card.tip == sub_word).all())
        return cards

    @classmethod
    def create_card(cls, user_id, word, translation, tip):
        card = Card(user_id, word, translation, tip)
        db.session.add(card)
        db.session.commit()
        return card

    def update(self, user_id, word, translation, tip):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('no_find_id.html')
        return self


@app.route('/')
def home():
    return render_template('home.html')


# User func ------------------------------------------------------------
@app.route('/user')
def user():
    users_list = User.get_all()
    return render_template('user/user_list.html', users=users_list)


@app.route('/user/<int:user_id>')
def get_user_id(user_id):
    user = User.get_by_id(user_id)
    if user:
        return render_template('user/user_info.html', user=user)
    return render_template('home.html')


@app.route('/user/create', methods=["POST", "GET"])
def user_create():
    if request.method == "GET":
        return render_template('user/user_create.html')
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        user = User.create_user(email, username, password)
        return redirect(url_for("get_user_id", user_id=user.id))


@app.route('/user/<int:user_id>/edit', methods=["POST", "GET"])
def user_update(user_id):
    user = User.get_by_id(user_id)
    if not user:
        return render_template('no_find_id.html')
    if request.method == "GET":
        return render_template('user/user_edit.html', user=user)
    if request.method == "POST":
        email = request.form["email"]
        username = request.form["username"]
        password = request.form["password"]
        user.update(email, username, password)
        return redirect(url_for("get_user_id", user_id=user.id))

    return render_template('home.html')


@app.route('/user/<int:user_id>/delete')
def user_delete(user_id):
    user = User.get_by_id(user_id)
    deck = Deck.get_all_deck_user_id(user_id)
    cards = Card.get_all_card_user_id(user_id)
    if not user:
        return render_template('no_find_id.html')
    cards.delete()
    deck.delete()
    user.delete()
    return redirect("/user")


# Deck func-------------------------------------------------------------
@app.route('/deck')
def deck():
    decks_list = Deck.get_all()
    return render_template('deck/deck_list.html', decks=decks_list)


@app.route('/deck/<int:deck_id>')
def get_deck_id(deck_id):
    deck = Deck.get_by_id(deck_id)
    if deck:
        return render_template('deck/deck_info.html', deck=deck)
    return render_template('home.html')


@app.route('/deck/create', methods=["POST", "GET"])
def deck_create():
    if request.method == "GET":
        return render_template('deck/deck_create.html')
    if request.method == "POST":
        name = request.form["name"]
        user_id = request.form["user_id"]
        user = db.session.query(User, Deck).join(Deck, Deck.user_id == User.id).first()
        if not user:
            return render_template('no_find_id.html')
        else:
            deck = Deck.create_deck(name, user_id)
            return redirect(url_for("get_deck_id", deck_id=deck.id))


@app.route('/deck/<int:deck_id>/edit', methods=["POST", "GET"])
def deck_update(deck_id):
    deck = Deck.get_by_id(deck_id)
    if not deck:
        return render_template('no_find_id.html')
    if request.method == "GET":
        return render_template('deck/deck_edit.html', deck=deck)
    if request.method == "POST":
        name = request.form["name"]
        user_id = request.form["user_id"]
        deck.update(name, user_id)
        return redirect(url_for("get_deck_id", deck_id=deck.id))
    return render_template('home.html')


@app.route('/deck/<int:deck_id>/delete')
def deck_delete(deck_id):
    deck = Deck.get_by_id(deck_id)
    cards = Card.get_all_card_user_id(deck.user_id)
    if not deck:
        return render_template('no_find_id.html')
    cards.delete()
    deck.delete()
    return redirect("/deck")


# Card func-----------------------------------------------------------------------
@app.route('/card')
def card():
    cards_list = Card.get_all()
    return render_template('card/card_list.html', cards=cards_list)


@app.route('/card/<int:card_id>')
def get_card_id(card_id):
    card = Card.get_by_id(card_id)
    if card:
        return render_template('card/card_info.html', card=card)
    return render_template('home.html')


@app.route('/card/create', methods=["POST", "GET"])
def card_create():
    if request.method == "GET":
        return render_template('card/card_create.html')
    if request.method == "POST":
        user_id = request.form["user_id"]
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        user = db.session.query(User, Card).join(Card, Card.user_id == User.id).first()
        if not user:
            return render_template('no_find_id.html')
        else:
            card = Card.create_card(user_id, word, translation, tip)
            return redirect(url_for("get_card_id", card_id=card.id))


@app.route('/card/<int:card_id>/edit', methods=["POST", "GET"])
def card_update(card_id):
    card = Card.get_by_id(card_id)
    if not card:
        return render_template('no_find_id.html')
    if request.method == "GET":
        return render_template('card/card_edit.html', card=card)
    if request.method == "POST":
        user_id = request.form["user_id"]
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        card.update(user_id, word, translation, tip)
        return redirect(url_for("get_card_id", card_id=card.id))
    return render_template('home.html')


@app.route('/card/<int:card_id>/delete')
def card_delete(card_id):
    card = Card.get_by_id(card_id)
    if not card:
        return render_template('no_find_id.html')
    card.delete()
    return redirect("/card")


@app.route('/card/filter', methods=["POST", "GET"])
def cards_filter():
    cards_list = Card.get_all()
    if not cards_list:
        return render_template('no_find_id.html')
    if request.method == "GET":
        return render_template('card/card_list.html', cards=cards_list)
    if request.method == "POST":
        sub_word = request.form["sub_word"]
        cards_tuple = Card.card_filter(sub_word)
        return render_template('card/card_list.html', cards=cards_tuple)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
