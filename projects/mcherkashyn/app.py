from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_



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
    name = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"{self.id} {self.name}"

    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.password}"

    @classmethod
    def get_by_id(cls, id):
        user = db.session.query(User).filter(User.id == id).first()
        return user

    @classmethod
    def get_all(cls):
        users = db.session.execute(db.select(User).order_by(User.name)).scalars()
        return users

    @classmethod
    def create(cls, name, email, password):
        user = User(name, email, password)
        db.session.add(user)
        db.session.commit()
        return user

    def update(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()
        return self

    def change_password(self, password):
        self.password = password
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as error:
            print(error)
        return self



class Deck(db.Model):
    __tablename__ = "decks"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"{self.id} {self.name}"

    def __str__(self):
        return f"{self.id} {self.name} {self.user_id}"

    @classmethod
    def get_by_id(cls, id):
        deck = db.session.query(Deck).filter(Deck.id == id).first()
        return deck

    @classmethod
    def get_all(cls):
        decks = db.session.execute(db.select(Deck).order_by(Deck.name)).scalars()
        return decks

    @classmethod
    def create(cls, name, user_id):
        deck = Deck(name, user_id)
        db.session.add(deck)
        db.session.commit()
        return deck

    def update(self, name):
        self.name = name
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        try:
            db.session.delete(self)
            db.session.commit()
        except Exception as error:
            print(error)
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

    def __repr__(self):
        return f"{self.id} {self.user_id}"

    def __str__(self):
        return f"{self.id} {self.user_id} {self.word} {self.translation} {self.tip}"

    @classmethod
    def get_by_id(cls, id):
        card = db.session.query(Card).filter(Card.id == id).first()
        return card

    @classmethod
    def get_all(cls):
        cards = db.session.execute(db.select(Card).order_by(Card.user_id)).scalars()
        return cards

    @classmethod
    def create(cls, user_id, word, translation, tip):
        card = Card(user_id, word, translation, tip)
        db.session.add(card)
        db.session.commit()
        return card

    @classmethod
    def card_filter(cls, sub_word):
        cards = tuple(db.session.query(Card).filter(or_(Card.word.ilike(f"%{sub_word}%"), Card.tip.ilike(f"%{sub_word}%"), Card.translation.ilike(f"%{sub_word}%"))).all())
        return cards

    def update(self, word, translation, tip):
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
        except Exception as error:
            print(error)
        return self





@app.route('/')
def home():
    return render_template('home.html')



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
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        user = User.create(name, email, password)
        return redirect(url_for("get_user_id", user_id=user.id))


@app.route('/user/<int:user_id>/edit_name', methods=["POST", "GET"])
def user_update_name(user_id):
    user = User.get_by_id(user_id)
    if not user:
        return render_template('error.html')
    if request.method == "GET":
        return render_template('user/user_update_name.html', user=user)
    if request.method == "POST":
        name = request.form["name"]
        user.update(name)
        return redirect(url_for("get_user_id", user_id=user.id))
    else:
        return render_template('error.html')

    return render_template('home.html')


@app.route('/user/<int:user_id>/change_password', methods=["POST", "GET"])
def user_change_password(user_id):
    user = User.get_by_id(user_id)
    password = user.password
    if not user:
        return render_template('error.html')
    if request.method == "GET":
        return render_template('user/user_change_password.html', user=user)
    if request.method == "POST":
        old_password = request.form["old_password"]
        new_password = request.form["new_password"]
        if old_password == password:
            user.change_password(new_password)
            return redirect(url_for("get_user_id", user_id=user.id))
    else:
        return render_template('error.html')

    return render_template('home.html')


@app.route('/user/<int:user_id>/delete')
def user_delete_by_id(user_id):
        user = User.get_by_id(user_id)
        if not user:
            return render_template('error.html')
        user.delete()
        return redirect("/user")



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
    try:
            if request.method == "GET":
                return render_template('deck/deck_create.html')
            if request.method == "POST":
                name = request.form["name"]
                user_id = request.form["user_id"]
                deck = Deck.create(name, user_id)
                return redirect(url_for("get_deck_id", deck_id=deck.id))
    except:
        return render_template('error.html')


@app.route('/deck/<int:deck_id>/edit_name', methods=["POST", "GET"])
def deck_update_name(deck_id):
    deck = Deck.get_by_id(deck_id)
    if not deck:
        return render_template('error.html')
    if request.method == "GET":
        return render_template('deck/deck_update_name.html', deck=deck)
    if request.method == "POST":
        name = request.form["name"]
        deck.update(name)
        return redirect(url_for("get_deck_id", deck_id=deck.id))
    else:
        return render_template('error.html')


@app.route('/deck/<int:deck_id>/delete')
def deck_delete_by_id(deck_id):
    deck = Deck.get_by_id(deck_id)
    if not deck:
        return render_template('error.html')
    deck.delete()
    return redirect("/deck")



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
    try:
            if request.method == "GET":
                return render_template('card/card_create.html')
            if request.method == "POST":
                user_id = request.form["user_id"]
                word = request.form["word"]
                translation = request.form["translation"]
                tip = request.form["tip"]
                card = Card.create(user_id, word, translation, tip)
                return redirect(url_for("get_card_id", card_id=card.id))
    except:
        return render_template('error.html')

@app.route('/card/filter', methods=["POST", "GET"])
def cards_filter():
    cards_list = Card.get_all()
    if not cards_list:
        return render_template('error.html')
    if request.method == "GET":
        return render_template('card/card_list.html', cards=cards_list)
    if request.method == "POST":
        sub_word = request.form["sub_word"]
        cards = Card.card_filter(sub_word)
        return render_template('card/card_list.html', cards=cards)


@app.route('/card/<int:card_id>/update', methods=["POST", "GET"])
def card_update(card_id):
    card = Card.get_by_id(card_id)
    if not card:
        return render_template('error.html')
    if request.method == "GET":
        return render_template('card/card_update.html', card=card)
    if request.method == "POST":
        word = request.form["word"]
        translation = request.form["translation"]
        tip = request.form["tip"]
        card.update(word, translation, tip)
        return redirect(url_for("get_card_id", card_id=card.id))
    else:
        return render_template('error.html')


@app.route('/card/<int:card_id>/delete')
def card_delete_by_id(card_id):
    card = Card.get_by_id(card_id)
    if not card:
        return render_template('error.html')
    card.delete()
    return redirect("/card")





if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
