from sqlalchemy import create_engine
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

dialect = "-----------------"
username = "----------"
password = "----"
host = "-----------"
port = "----"
database = "----------"
engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(autoflush=False, bind=engine)

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return f'{self.id}, {self.name}'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.email}, {self.password}'


class Deck(Base):
    __tablename__ = "decks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))

    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id

    def __repr__(self):
        return f'{self.id}, {self.name}'

    def __str__(self):
        return f'{self.id}, {self.name}, {self.user_id}'


class Card(Base):
    __tablename__ = "cards"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    word = Column(String)
    translation = Column(String)
    tip = Column(String)

    def __init__(self, user_id, word, translation, tip):
        self.user_id = user_id
        self.word = word
        self.translation = translation
        self.tip = tip

    def __str__(self):
        return f'{self.id}, {self.user_id=}, {self.word},  {self.translation}, {self.tip}'

    def __repr__(self):
        return f'{self.id}, {self.word},  {self.translation}, {self.tip}'


# User func----------------------------------------------------------------
def create_user(name, email, password):
    user = User(name, email, password)
    session.add(user)
    session.commit()


def get_by_id_user(user):
    with session:
        user = session.query(User).filter(User.id == user.id).first()
        if user is not None:
            user_id = user.id

    return user_id


def user_update_name(user_id, name):
    with session:
        user = session.query(User).filter(User.id == user_id).first()
        if user is not None:
            print(f"{user.id}.{user.name} ({user.password})")
            user.name = name
            print(f"{user.id}.{user.name} ({user.password})")
            session.commit()
        else:
            print('Пользователя нет в списке')


def user_change_password(user_id, old_password, new_password):
    with session:
        user = session.query(User).filter(User.id == user_id).first()
        if user is not None and old_password == user.password:
            print(f"{user.id}.{user.name} ({user.password})")
            user.password = new_password
            print(f"{user.id}.{user.name} ({user.password})")
            session.commit()
            return True
        else:
            return False


def user_delete_by_id(user_id):
    with session:
        user = session.query(User).filter(User.id == user_id).first()
        if user is not None:
            print(f"{user.id}.{user.name} ({user.password})")
            session.delete(user)
            print(f"{user.id}.{user.name} ({user.password})")
            session.commit()
            return True
        else:
            return False


# Deck func_____________________________________________________________________

def deck_create(name, user_id):
    deck = Deck(name, user_id)
    session.add(deck)
    session.commit()


def deck_get_by_id(deck):
    with session:
        deck = session.query(Deck).filter(Deck.id == deck.id).first()
        if deck is not None:
            deck_id = deck.id

    return deck_id


def deck_update(deck_id, name):
    with session:
        deck = session.query(Deck).filter(Deck.id == deck_id).first()
        if deck is not None:
            print(f"{deck.id}.{deck.name}")
            deck.name = name
            print(f"{deck.id}.{deck.name}")
            session.commit()
        else:
            print('Колоды нет в списке')


def deck_delete_by_id(deck_id):
    with session:
        deck = session.query(Deck).filter(Deck.id == deck_id).first()
        if deck is not None:
            print(f"{deck.id}.{deck.name}")
            session.delete(deck)
            print(f"{deck.id}.{deck.name}")
            session.commit()
            return True
        else:
            return False


# Card func_______________________________________________________________________
def card_create(user_id, word, translation, tip):
    card = Card(user_id, word, translation, tip)
    session.add(card)
    session.commit()


def card_get_by_id_(card):
    with session:
        card = session.query(Card).filter(Card.id == card.id).first()
        if card is not None:
            card_id = card.id

    return card_id


def card_filter(sub_word):
    with session:
        cards = tuple(session.query(Card).filter(
            Card.word == sub_word or Card.translation == sub_word or Card.tip == sub_word).all())
        if cards is not None:
            for c in cards:
                print(c)
            else:
                print('Карты нет в списке')
    return cards


def update_card(card_id, word=None, translation=None, tip=None):
    with session:
        card = session.query(Card).filter(Card.id == card_id).first()
        if Card is not None:
            if word is not None:
                card.word = word
            elif translation is not None:
                card.translation = translation
            elif tip is not None:
                card.tip = tip
        else:
            print('Карты нет в списке')
        session.commit()


def card_delete_by_id(card_id):
    with session:
        card = session.query(Card).filter(Card.id == card_id).first()
        if card is not None:
            print(f"{card.id}, {card.word}, {card.translation}, {card.tip}")
            session.delete(card)
            print(f"{card.id}, {card.word}, {card.translation}, {card.tip}")
            session.commit()
            return True
        else:
            return False


Base.metadata.create_all(engine)

session = Session()

create_user('uS1', 'tiger@gmail.com', 'port')
create_user('Us2', 'lion@gmail.com', 'dock')
create_user('US3', 'puma@gmail.com', 'rog')

people = session.query(User).all()
for p in people:
    print(f'{p.id}: {p.name}')
id_user = int(input('id_user '))
user = session.query(User).filter(User.id == id_user).first()
user_id = get_by_id_user(user)

user_update_name(user_id, 'name1')

user_change_password(user_id, 'root', '1234')

user_delete_by_id(3)
print(User)

# Deck------------------------------------------------------------
deck_create('name', 1)
deck_create('good', 2)
deck_create('not good', 1)

decks = session.query(Deck).all()
for d in decks:
    print(f'{d.id}: {d.name}')
id_deck = int(input('id_deck '))
deck = session.query(Deck).filter(Deck.id == id_deck).first()
deck_id = deck_get_by_id(deck)

deck_update(deck_id, 'deck1')

deck_delete_by_id(3)
print(Deck)

# Card----------------------------------------------------------
card_create(1, 'Way', 'Путь', '----')
card_create(2, 'Goal', 'Цель', '----')

cards = session.query(Card).all()
for c in cards:
    print(f'{c.id}: {c.word}, {c.translation}, {c.tip}')
id_card = int(input('id_card '))
card = session.query(Card).filter(Card.id == id_card).first()
card_id = card_get_by_id_(card)

word = input('word ')
translation = input('translation ')
tip = input('tip ')
update_card(card_id, word, translation, tip)

card_delete_by_id(2)
