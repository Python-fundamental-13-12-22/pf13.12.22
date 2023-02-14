from sqlalchemy.orm._orm_constructors import relationship, backref
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import create_engine, event
#from sqlalchemy import update
import string
import secrets

try:
    from local_settings import *
except:
    print("can't find local_settings")

# https://docs.sqlalchemy.org/en/20/core/engines.html
engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), index=True)
    email = Column(String(16), index=True)
    password = Column(String(12), index=True)


    def __repr__(self):
        return f"{self.id} {self.name} {self.email} "
    def __str__(self):
        return f"{self.id} {self.name} {self.email}  {self.password}"

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String(16), index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, backref=backref('decks', order_by=user_id))
    def __repr__(self):
        return f"{self.id} {self.name} "
    def __str__(self):
        return f"{self.id} {self.name} "

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, backref=backref('cards', order_by=user_id))
    word = Column(String(16), index=True)
    translation = Column(String(16), index=True)
    tip = Column(String(16), index=True)
    def __repr__(self):
        return f"{self.id} {self.word} {self.translation}  {self.tip} "
    def __str__(self):
        return f"{self.id} {self.word} {self.translation}  {self.tip} "

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
#print(generate_password())

Base.metadata.create_all(engine)
session = Session()


def user_create(name, email, password):
    result = User(name=name, email=email, password=password)
    session.add(result)
    session.commit()
def user_get_by_id(user_id):
    users = session.query(User).filter(User.id == user_id)
    users = users.all()
    return users
def user_update_name(user_id, name):
    if (session.query(User).filter(User.id == user_id)).first() != None:
        session.query(User).filter(User.id == user_id).update({User.name: name})
        session.commit()
    else:
        print(f"error user id = {(session.query(User).filter(User.id == user_id)).first()}  ")
def user_change_password(user_id, old_password, new_password):
        if (session.query(User).filter(User.id == user_id)).first().password == old_password and (session.query(User).filter(User.id == user_id)).first() != None:
            session.query(User).filter(User.id == user_id).update({User.password: new_password})
            session.commit()
        else:
            print(f"Please input coorrect old password:  ")

def user_delete_by_id(user_id):
    #print((session.query(User).filter(User.id == user_id)).first())
    if (session.query(User).filter(User.id == user_id)).first() != None:
        session.query(User).filter(User.id == user_id).delete()
        session.commit()
    else:
        print(f"error user id = {(session.query(User).filter(User.id == user_id)).first()}  ")

def deck_create(name, user_id):
    result = Deck(name=name, user_id=user_id)
    session.add(result)
    session.commit()
def deck_get_by_id(deck_id):
    decks = session.query(Deck).filter(Deck.id == deck_id)
    decks = decks.all()
    return decks
def deck_update(deck_id, name):
    if (session.query(Deck).filter(Deck.id == deck_id)).first() != None:
        session.query(Deck).filter(Deck.id == deck_id).update({Deck.name: name})
        session.commit()
    else:
        print(f"error user id = {(session.query(Deck).filter(Deck.id == deck_id)).first()}  ")
def deck_delete_by_id(deck_id):
    if (session.query(Deck).filter(Deck.id == deck_id)).first() != None:
        session.query(Deck).filter(Deck.id == deck_id).delete()
        session.commit()
    else:
        print(f"error user id = {(session.query(Deck).filter(Deck.id == deck_id)).first()}  ")
def card_create(user_id, word, translation, tip):
    result = Card(user_id=user_id, word=word, translation=translation, tip=tip)
    session.add(result)
    session.commit()
def card_get_by_id(cards_id):
    cards = session.query(Card).filter(Card.id == cards_id)
    cards = cards.all()
    return cards
def card_filter(sub_word):
    cards = session.query(Card).filter(Card.word.like(sub_word)) or session.query(Card).filter(Card.translation.like(sub_word)) or session.query(Card).filter(Card.tip.like(sub_word))
    print(cards)
    cards = cards.all()
    return cards

def card_update(card_id, word=None, translation=None, tip=None):
    if (session.query(Card).filter(Card.id == card_id)).first() != None:
        session.query(Card).filter(Card.id == card_id).update({Card.word: word})
        session.query(Card).filter(Card.id == card_id).update({Card.translation: translation})
        session.query(Card).filter(Card.id == card_id).update({Card.tip: tip})
        session.commit()
    else:
        print(f"error user id = {(session.query(Card).filter(Deck.id == card_id)).first()}  ")

def card_delete_by_id(card_id):
    if (session.query(Card).filter(Card.id == card_id)).first() != None:
        session.query(Card).filter(Card.id == card_id).delete()
        session.commit()
    else:
        print(f"error user id = {(session.query(Card).filter(Deck.id == card_id)).first()}  ")
#--- user
#name = input('users name: ')
#email = input('email: ')
#password = generate_password()
#user_create(name, email, password)
print(user_get_by_id(2))
#user_update_name(1, "Taras++update")
#print(user_update_name(2, "Vas++update"))
#user_change_password(1, '1111111', 'ndwnwdnwj777')
#user_delete_by_id(5)

#--- deck
#deck_create('Колода1', 6)
#print(deck_get_by_id(2))
#deck_update(2, 'Колода2_1')
#deck_delete_by_id(5)


#--- card
#card_create(2, "Hello", "Привіт", "підказка")
#card_create(2, "Hello", "Hello123", "Hello124")
#print(card_get_by_id(1))
#print(card_filter('Hello'))
#card_update(2, 'sss', 'sds', 'sfd')
#card_delete_by_id(2)