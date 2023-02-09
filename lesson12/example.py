from sqlalchemy import create_engine
from sqlalchemy.orm._orm_constructors import relationship, backref
from sqlalchemy.orm.decl_api import declarative_base
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String

dialect = "postgresql"
username = "postgres"
password = "19341934"
host = "localhost"
port = "5432"
database = "pf13"
# https://docs.sqlalchemy.org/en/20/core/engines.html
engine = create_engine(f"{dialect}://{username}:{password}@{host}:{port}/{database}")
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    username = Column(String)
    age = Column(Integer)
    def __repr__(self):
        return f"{self.id} {self.email}"
    def __str__(self):
        return f"{self.id} {self.email} {self.username} {self.books}"

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User, backref=backref('books',order_by=title))
    def __repr__(self):
        return f"{self.id} {self.title}"

Base.metadata.create_all(engine)

session = Session()
user1 = User(email="email1@com.com", username="user1", age=18)
user2 = User(email="email2@com.com", username="user2", age=28)
user3 = User(email="email3@com.com", username="user3", age=13)
print(user1)
book1 = Book(title="title1", description="description1", user=user1)
book2 = Book(title="title2", description="description2", user=user1)
book3 = Book(title="title3", description="description3", user=user2)
session.add(user1)
session.add_all([user2, user3])
session.add_all([book1, book2, book3])
session.commit()
print(user1)

users = session.query(User).filter(User.email == "email1@com.com")
print(users)
users = users.all()
print(users)
