from datetime import datetime
from fitness import db, login_manager
from flask_login import UserMixin


# Require user login to query data
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# User database model with id, first name, last name, email, password and so on
# that store user information
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(60), nullable=False)
    lname = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    ##image_file = db.Column(db.String(20), unique=True, default='avatar.png')
    password = db.Column(db.String(60), nullable=False)
    post_attribute = db.relationship('Post', backref='author', lazy=True)
    user_data = db.relationship('UserData', backref='user_database', lazy=True)
    user_perk = db.Column(db.Integer, nullable=False)
    consumed = db.Column(db.Integer, nullable=True)
    burned = db.Column(db.Integer, nullable=True)
    calories = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}','{self.email}')"
        ##return f"User('{self.email}', '{self.image_file}')"


# Posting database model with id, first name, last name, email, password and so on
# that store user posts
class Post(db.Model):
    __searchable__ = ['title', 'content']
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.data_posted}')"


class UserData(db.Model):
    dataId = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.today())
    consumed = db.Column(db.Integer, nullable=True)
    burned = db.Column(db.Integer, nullable=True)
    cardio = db.Column(db.Integer, nullable=True)
    strength = db.Column(db.Integer, nullable=True)
    rest = db.Column(db.Integer, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', foreign_keys = user_id)
