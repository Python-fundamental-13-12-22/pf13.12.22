from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import or_

dialect = "*"
username = "*"
password = "*"
host = "*"
port = "5432"
database = "linguist"

engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)
    def __repr__(self):
        return f"{self.id} {self.name} {self.email} {self.password}"

class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    def __repr__(self):
        return f"{self.id} {self.name} {self.user_id}"

class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    def __repr__(self):
        return f"{self.id} {self.user_id} {self.word} {self.translation} {self.tip}"

Base.metadata.create_all(engine)

def user_create(name, email, password):
    session = Session()
    new_user = User(
        name=name,
        email=email,
        password=password
    )
    session.add(new_user)
    session.commit()
    return new_user

def user_get_by_id(user_id):
    session = Session()
    user = session.get(User, user_id)
    return user

def user_update_name(user_id, name):
    session = Session()
    new = session.get(User, user_id)
    new.name = name
    session.add(new)
    session.commit()
    return new

def user_change_password(user_id, old_password, new_password):
    session = Session()
    get_by_id = session.get(User, user_id)
    if old_password == get_by_id.password and user_id == get_by_id.id:
        get_by_id.password = new_password
        session.add(get_by_id)
        session.commit()
        return get_by_id

def user_delete_by_id(user_id):
    session = Session()
    get_by_id = session.get(User, user_id)
    session.delete(get_by_id)
    session.commit()
    print("deleted")

def deck_create(name, user_id):
    session = Session()
    new_deck = Deck(
        name=name,
        user_id=user_id
    )
    session.add(new_deck)
    session.commit()
    return new_deck

def deck_get_by_id(id):
    session = Session()
    deck = session.get(Deck, id)
    return deck

def deck_update_name(id, name):
    session = Session()
    new = session.get(Deck, id)
    new.name = name
    session.add(new)
    session.commit()
    return new

def deck_delete_by_id(id):
    session = Session()
    get_by_id = session.get(Deck, id)
    session.delete(get_by_id)
    session.commit()
    print("deleted")

def card_create(user_id, word, translation, tip):
    session = Session()
    new_card = Card(
        user_id=user_id,
        word=word,
        translation=translation,
        tip=tip
    )
    session.add(new_card)
    session.commit()
    return new_card

def card_get_by_id(id):
    session = Session()
    card = session.get(Card, id)
    return card

def card_filter(sub_word):
    session = Session()
    cards = tuple(session.query(Card).filter(or_(Card.word.ilike(f"%{sub_word}%"), Card.tip.ilike(f"%{sub_word}%"), Card.translation.ilike(f"%{sub_word}%"))).all())
    return cards

def card_update(id, word=None, translation=None, tip=None):
    session = Session()
    new = session.get(Card, id)
    new.word = word
    new.translation = translation
    new.tip = tip
    session.add(new)
    session.commit()
    return new

def card_delete_by_id(id):
    session = Session()
    get_by_id = session.get(Card, id)
    session.delete(get_by_id)
    session.commit()
    print("deleted")

Base.metadata.create_all(engine)

print(user_create("Dmytro", "dmytro@email.com", "helloworld"))

print(user_create("Petro", "petro@email.com", "helloworld2"))

print(user_create("Sashko", "sashko@email.com", "helloworld3"))

print(user_delete_by_id(4))

print(user_delete_by_id(5))

print(user_change_password(1, "helloworld", "ok"))

print(user_update_name(2, "Andrew"))

print(user_get_by_id(1))

print(deck_create("new_deck", 1))

print(deck_create("new_deck2", 2))

print(deck_get_by_id(1))

print(deck_update_name(1, "new_deck1"))

print(deck_delete_by_id(1))

print(card_create(6, "anothertarget", "translation1", "tip1"))

print(card_create(7, "word2", "target", "tip2"))

print(card_create(8, "word3", "translation3", "target"))

print(card_filter("target"))

print(card_update(1, "new_word", "new_translation"))

print(card_delete_by_id(3))
