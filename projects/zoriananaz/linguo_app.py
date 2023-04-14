from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, or_
from sqlalchemy.orm import backref
#import string
#import secrets

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
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password = db.Column(db.String(20))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.id} {self.name} {self.email} {self.password}"

    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.password}"

    def user_update(self, name, email):
        self.name = name
        self.email = email
        self.password = password
        db.session.add(self)
        db.session.commit()
        return self

    def user_change_password(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def user_create(cls, name, email, password):
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_all(cls):
        users = db.session.execute(db.select(User).order_by(User.name)).scalars()
        return users

    @classmethod
    def user_get_by_id(cls, id):
        user = db.session.query(User).filter(User.id == id).first()
        return user

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('/error.html')
        return self

    """"@classmethod
    def user_change_password(cls, user_id, password, enter_new_password):
        user = db.session.get(User, user_id)
        user.password = enter_new_password
        if enter_new_password != password:
            user.password = enter_new_password
            db.session.add(user)
            db.session.commit()
            return user
        else:
            return False"""


@app.route('/user_change_password/<int:user_id>', methods=["POST", "GET"])
def change_password(user_id):
    user = User.user_get_by_id(user_id)
    if not user_id:
        return render_template('/error.html')
    if request.method == "GET":
        return render_template('/user/user_change_password.html', user=user)
    if request.method == "POST":
        #user_id = request.form["user_id"]
        name = request.form["name"]
        email = request.form["email"]
        enter_new_password = request.form["enter_new_password"]
        confirm_new_password = request.form["confirm_new_password"]
        if enter_new_password == confirm_new_password:
            password = enter_new_password
            user.user_change_password(name, email, password)
            return redirect(url_for("get_user_id", user_id=user.id))
    return render_template('home.html')

@app.route('/')
def hello_world():
    return render_template('home.html')

""""@app.route('/user')
def users():
    return 'User'"""


@app.route('/create_user', methods=["POST", "GET"])
def create_user():
    if request.method == "GET":
        return render_template('/user/create_user.html')
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]
        if password == confirm_password:
            user = User.user_create(name, email, password)
            return redirect(url_for("get_user_id", user_id=user.id))
        else:
            return redirect("/error.html")
    return render_template('home.html')



@app.route('/user_info/<int:user_id>')
def get_user_id(user_id):
    user = User.user_get_by_id(user_id)
    if user:
        return render_template('user/user_info.html', user=user)
    return render_template('home.html')


@app.route('/user_info/<int:user_id>/update', methods=["POST", "GET"])
def update_user(user_id):
    user = User.user_get_by_id(user_id)
    if not user:
        return render_template('/error.html')
    if request.method == "GET":
        return render_template('/user/update_user.html', user=user)
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        user.user_update(name, email)
        return redirect(url_for("get_user_id", user_id=user.id))
    return render_template('home.html')





@app.route('/users_all')
def get_users():
    users = db.session.execute(db.select(User).order_by(User.name)).scalars()
    return render_template('user/users_all.html', users=users)


@app.route('/users_all/<int:user_id>/delete', methods=["POST", "GET"])
def delete_user(user_id):
    user = User.user_get_by_id(user_id)
    if not user:
        return render_template('/error.html')
    user.delete()
    return redirect(url_for("get_users", user_id=user.id))


class Deck(db.Model):
    __tablename__ = "deck"
    id = db.Column(Integer, primary_key=True)
    topic = db.Column(String(20))
    user_id = db.Column(Integer, ForeignKey('users.id'))
    user = db.relationship(User, backref=backref('deck', order_by=user_id))

    def __init__(self, topic, user_id):
        self.topic = topic
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id}{self.topic}{self.user_id}"

    def __str__(self):
        return f"{self.id} {self.topic} {self.user_id}"

    @classmethod
    def deck_create(cls, topic, user_id):
        deck = Deck(topic, user_id)
        db.session.add(deck)
        db.session.commit()
        return deck

    @classmethod
    def get_all_decks(cls):
        decks = db.session.execute(db.select(Deck).order_by(Deck.topic)).scalars()
        return decks

    @classmethod
    def deck_get_by_id(cls, id):
        deck = db.session.query(Deck).filter(Deck.id == id).first()
        if deck:
            return deck
        return render_template('home.html')

    """@classmethod
    def deck_update(cls, deck_id, topic):
        deck_topic = db.session.get(Deck, deck_id)
        deck_topic.topic = topic
        db.session.add(deck_topic)
        db.session.commit()
        return deck_topic"""

    def deck_update(self, topic):
        self.topic = topic
        db.session.add(self)
        db.session.commit()
        return self

    def deck_delete_by_id(self):
        db.session.delete(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('/error.html')
        return self


@app.route('/deck_create',  methods=["POST", "GET"])
def create_deck():
    if request.method == "GET":
        return render_template('/deck/deck_create.html')
    if request.method == "POST":
        topic = request.form["topic"]
        user_id = request.form["user_id"]
        deck = Deck.deck_create(topic, user_id)
        return redirect(url_for("get_id_deck", deck_id=deck.id))


@app.route('/deck/<int:deck_id>/update', methods=["POST", "GET"])
def update_deck(deck_id):
    deck = Deck.deck_get_by_id(deck_id)
    if not deck:
        return render_template('/error.html')
    if request.method == "GET":
        return render_template('/deck/deck_update.html', deck=deck)
    if request.method == "POST":
        topic = request.form["topic"]
        deck.deck_update(topic)
        return redirect(url_for("get_id_deck", deck_id=deck.id))
    return render_template('home.html')


@app.route('/decks_all')
def get_all_decks():
    decks = db.session.execute(db.select(Deck).order_by(Deck.topic)).scalars()
    return render_template('deck/decks_all.html', decks=decks)


@app.route('/deck/<int:deck_id>')
def get_id_deck(deck_id):
    deck = Deck.deck_get_by_id(deck_id)
    if deck:
        return render_template('deck/deck_info.html', deck=deck)
    return render_template('home.html')


@app.route('/deck_all/<int:deck_id>/delete', methods=["POST", "GET"])
def delete_deck(deck_id):
    deck = Deck.deck_get_by_id(deck_id)
    if not deck:
        return render_template('error.html')
    deck.delete()
    return redirect(url_for("get_all_decks", deck=deck.id))


class Card(db.Model):
    __tablename__ = "card"
    id = db.Column(Integer, primary_key=True)
    user_id = db.Column(Integer, ForeignKey('users.id'))
    word = db.Column(String)
    translation = db.Column(String)
    tip = db.Column(String)
    topic = db.Column(String)
    user = db.relationship(User, backref=backref('card', order_by=user_id))

    def __init__(self, word, translation, tip, topic, user_id):
        self.word = word
        self.translation = translation
        self.tip = tip
        self.topic = topic
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id} {self.word}  {self.translation} {self.tip} {self.topic} {self.user_id}"

    def __str__(self):
        return f"{self.id} {self.word} {self.translation} {self.tip} {self.topic} {self.user_id}"

    @classmethod
    def card_create(cls, user_id, word, translation, tip, topic):
        card = Card(user_id=user_id, word=word, tip=tip, translation=translation, topic=topic)
        db.session.add(card)
        db.session.commit()
        return card

    @classmethod
    def get_cards(cls):
        cards = db.session.execute(db.select(Card).order_by(Card.id)).scalars()
        return cards

    @classmethod
    def card_get_by_id(cls, card_id):
        card = db.session.get(Card, card_id)
        return card

    @classmethod
    def card_filter(cls, sub_word):
        cards = tuple(db.session.query(Card).filter(or_(db.Card.word.ilike(f"%{sub_word}%"),
                                                     db.Card.translation.ilike(f"%{sub_word}%"),
                                                     db.Card.tip.ilike(f"%{sub_word}%"),
                                                     db.Card.topic.ilike(f"%{sub_word}%"))).all())
        return cards


    def card_update(self, word=None, translation=None, tip=None, topic=None):
        self.word = word
        self.translation = translation
        self.tip = tip
        self.topic = topic
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception:
            return render_template('/error.html')
        return self

    def card_delete_by_id(self):
        db.session.delete(self)
        db.session.commit()
        return self

@app.route('/cards_all/filter/<sub_word>', methods= ["GET", "POST"])
def filter_word():
    all_cards = Card.get_cards()
    if request.method == "GET":
        return render_template('card/ cards_all.html', cards=all_cards)
    if request.method == "POST":
        sub_word = request.form["sub_word"]
        all_cards = Card.card_filter(sub_word)
        return render_template('card/cards_all.html', cards=all_cards)


@app.route('/card_info/<int:card_id>/update', methods=["POST", "GET"])
def update_card(card_id):
    card = Card.card_get_by_id(card_id)
    if not card:
        return render_template('/error.html')
    if request.method == "GET":
        return render_template('/user/update_user.html', card=card)
    if request.method == "POST":
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        topic = request.form["topic"]
        card.card_update(word, translation, topic, tip)
        return redirect(url_for("card_get_by_id", card_id=card.id))
    return render_template('home.html')


@app.route('/cards_all/<int:card_id>/delete', methods=["POST", "GET"])
def card_delete(card_id):
    card = Card.card_get_by_id(card_id)
    if not card:
        render_template('/error.html')
    card.delete()
    return redirect('/card')


@app.route('/card_info/<int:card_id>')
def card_get_id(card_id):
    card = Card.card_get_by_id(card_id)
    if card:
        return render_template('card/card_info.html', card=card)
    return render_template('home.html')


@app.route('/cards_all')
def get_all_cards():
    cards = db.session.execute(db.select(Card).order_by(Card.id)).scalars()
    return render_template('card/cards_all.html', cards=cards)


@app.route('/card_create', methods=["POST", "GET"])
def create_card():
    if request.method == "GET":
        return render_template('/card/card_create.html')
    if request.method == "POST":
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        topic = request.form["topic"]
        user_id = request.form["user_id"]
        card = Card.card_create(user_id, word, tip, translation,  topic)
        return redirect(url_for("card_get_id", card_id=card.id))




if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
