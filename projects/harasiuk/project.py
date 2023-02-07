from sqlalchemy import create_engine
from sqlalchemy.orm import relationship, backref
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import or_

dialect = "postgresql"
driever = "psycopg2"
username = "postgres"
password1 = "root"
host = "localhost"
port = "5432"
database = "project"
# https://docs.sqlalchemy.org/en/20/core/engines.html
engine = create_engine(f"{dialect}://{username}:{password1}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f"<{self.id}. {self.name}>"


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f"<{self.id}. {self.name}>"


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    def __init__(self, user_id, word, tip, translation):
        self.user_id = user_id
        self.word = word
        self.tip = tip
        self.translation = translation

    def __repr__(self):
        return f"<{self.id}. {self.word}>"


def deck_create(name, user_id):
    deck = Deck(name=name, user_id=user_id)
    session = Session()
    session.add(deck)
    session.commit()
    return deck


def deck_get_by_id(deck_id):
    session = Session()
    deck = session.get(Deck, deck_id)
    return deck


def deck_update(deck_id, name):
    session = Session()
    deck = session.get(Deck, deck_id)
    deck.name = name
    session.add(deck)
    session.commit()
    return deck


def deck_delete_by_id(deck_id):
    session = Session()
    deck = session.get(Deck, deck_id)
    if deck:
        session.delete(deck)
        session.commit()
        return True
    else:
        return False


def card_create(user_id, word, translation, tip):
    card = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session = Session()
    session.add(card)
    session.commit()
    return card


def card_get_by_id(card_id):
    session = Session()
    card = session.get(Card, card_id)
    return card


def card_update(card_id, word=None, translation=None, tip=None):
    session = Session()
    card = session.get(Card, card_id)
    card.word = word
    card.translation = translation
    card.tip = tip
    session.add(card)
    session.commit()
    return card


def card_delete_by_id(card_id):
    session = Session()
    card = session.get(Card, card_id)
    if card:
        session.delete(card)
        session.commit()
        return True
    else:
        return False


def card_filter(sub_word):
    session = Session()
    cards = tuple(session.query(Card).filter(or_(
        Card.word.ilike(f"%{sub_word}%"),
        Card.tip.ilike(f"%{sub_word}%"),
        Card.translation.ilike(f"%{sub_word}%")
    )).all())
    return cards


def user_create(name, email, password):
    user = User(name=name, email=email, password=password)
    session = Session()
    session.add(user)
    session.commit()
    return


def user_get_by_id(user_id):
    session = Session()
    user = session.get(User, user_id)
    return user


def user_update_name(user_id, name):
    session = Session()
    user = session.get(User, user_id)
    user.name = name
    session.add(user)
    session.commit()


def user_change_password(user_id, old_password, new_password):
    session = Session()
    user = session.get(User, user_id)
    if old_password == user.password and user:
        user.password = new_password
        session.add(user)
        session.commit()
        return True
    else:
        return False


def user_delete_by_id(user_id):
    session = Session()
    user = session.get(User, user_id)
    if user:
        session.delete(user)
        session.commit()
        return True
    else:
        return False


Base.metadata.create_all(engine)

user_create("User1", "user1@mail.com", "password1")
user_create("User2", "user2@mail.com", "password2")
user_create("User3", "user3@mail.com", "password3")
user_update_name(1, "user1_1")
user_change_password(1, "password1", "password1!")
user_delete_by_id(2)
print(user_change_password(1, "password1", "password1!"))
