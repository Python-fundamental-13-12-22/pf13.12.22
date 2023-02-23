from sqlalchemy import create_engine
from sqlalchemy.orm._orm_constructors import relationship, backref
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy import or_

dialect = "postgresql"
username = "postgres"
password = "pink"
host = "localhost"
port = "5432"
database = "linguo"
engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(autoflush=False, bind=engine)
session = Session()
Base = declarative_base()

Base.metadata.create_all(engine)

#USER_________________________________-


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __repr__(self):
        return f"{self.name} {self.email}"

    def __str__(self):
        return f"{self.id} {self.name} {self.email} {self.password}"


def user_create(name, email, password):
    user_new = User(name=name,
                    email=email,
                    password=password)
    session.add(user_new)
    session.commit()
    return user_new


def user_get_by_id(user_id):
    user = session.get(User, user_id)
    return user


def user_update_name(user_id, name):
    new_us = session.get(User, user_id)
    new_us.name = name
    session.add(new_us)
    session.commit()
    return new_us


def user_delete_by_id(user_id):
    user = session.get(User, user_id)
    session.delete(user)
    session.commit()
    return user


def user_change_password(user_id, old_password, new_password):
    user = session.get(User, user_id)
    user.password = old_password
    if old_password != new_password:
        user.password = new_password
        session.add(user)
        session.commit()
        return user
    else:
        return False


#DECK_________


class Deck(Base):
    __tablename__ = "deck"
    id = Column(Integer, primary_key=True)
    topic = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, backref=backref('users', order_by=user_id))

    def __repr__(self):
        return f"{self.id}{self.topic}{self.user_id}"

    def __str__(self):
        return f"{self.id} {self.topic} {self.user_id}"


def deck_create(topic, user_id):
    topic = Deck(topic=topic, user_id=user_id)
    session.add(topic)
    session.commit()
    return topic


def deck_get_by_id(deck_id):
    deck = session.get(Deck, deck_id)
    return deck


def deck_update(deck_id, topic):
    deck_topic = session.get(Deck, deck_id)
    deck_topic.topic = topic
    session.add(deck_topic)
    session.commit()
    return deck_topic


def deck_delete_by_id(deck_id):
    deck = session.get(Deck, deck_id)
    session.delete(deck)
    session.commit()
    return deck

#CARD________


class Card(Base):
    __tablename__ = "card"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)
    topic = Column(String,  ForeignKey('deck.topic'))
    user = relationship(Deck, backref=backref('deck', order_by=topic))

    def __repr__(self):
        return f"{self.id} {self.word}  {self.translation} {self.tip} {self.topic}"

    def __str__(self):
        return f"{self.id} {self.word} {self.translation} {self.tip} {self.topic}"


def card_create(user_id, word, translation, tip, topic):
    card = Card(user_id=user_id, word=word, tip=tip, translation=translation, topic=topic)
    session.add(card)
    session.commit()
    return card


def card_get_by_id(card_id):
    card = session.get(Card, card_id)
    return card


def card_filter(sub_word):
    cards = tuple(session.query(Card).filter(or_(Card.word.ilike(f"%{sub_word}%"),
                Card.translation.ilike(f"%{sub_word}%"),
                Card.tip.ilike(f"%{sub_word}%"),
                Card.topic.ilike(f"%{sub_word}%"))).all())
    return cards


def card_update(card_id, word=None, translation=None, tip=None, topic=None):
    new_card = session.get(Card, card_id)
    new_card.word = word
    new_card.translation = translation
    new_card.tip = tip
    new_card.topic =topic
    session.add(new_card)
    session.commit()
    return new_card


def card_delete_by_id(card_id):
    card = session.get(Card, card_id)
    session.delete(card)
    session.commit()
    return card

#print(user_create("Olga", "olga@gmail.com", "olg"))
#print(card_create(27, "yellow", "жовтий", "The sun is ...", "colors"))
#print(card_create(27, "black", "чорний", "The soil is ...", "colors"))
#print(card_create(28, "blue", "блакитний", "The sky is ...", "colors"))
#print(card_delete_by_id(4))
#print(deck_create("colors", 27))
#print(card_create(28, "winter", "зима", "When snowing weather...", "seasons"))
#print(deck_get_by_id(1))
#card_update(3,"red", "червоний", "The heard is ...", "colors" )
