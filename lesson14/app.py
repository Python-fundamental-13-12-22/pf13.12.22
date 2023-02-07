from flask import Flask, request, redirect
from flask.helpers import url_for
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy

dialect = "postgresql"
username = "postgres"
password = "root"
host = "localhost"
port = "5432"
database = "pf131222"
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
    age = db.Column(db.Integer)

    def __init__(self, email, username, age):
        self.email = email
        self.username = username
        self.age = age

    def __repr__(self):
        return f"{self.id} {self.email}"

    def __str__(self):
        return f"{self.id} {self.email} {self.username} {self.books}"

    @classmethod
    def get_by_id(cls, id):
        user = db.session.query(User).filter(User.id == id).first()
        return user

    @classmethod
    def get_all(cls):
        users = db.session.execute(db.select(User).order_by(User.username)).scalars()
        return users

    @classmethod
    def create(cls, email, username, age):
        user = User(email, username, age)
        db.session.add(user)
        db.session.commit()
        return user


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
        email = request.form["email"]
        username = request.form["username"]
        age = request.form["age"]
        user = User.create(email, username, age)
        return redirect(url_for("get_user_id", user_id=user.id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
