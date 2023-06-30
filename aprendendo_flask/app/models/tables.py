from app import db

class User(db.Model):
    __tablename__ = "users"
    id = db.column(db.Integer, primary_key = True)
    username = db.column(db.String, unique = True)
    password = db.column(db.String)
    email = db.column(db.String, unique = True)
    name = db.column(db.String)

    def __init__(self, username, password, email, name):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
    
    def __repr__(self):
        return "<User %r>" % self.username
    
class Post(db.Model):
    __tablename__ = "posts"
    id = db.column(db.Integer, primary_key = True)
    content = db.column(db.Text)
    user_id = db.column(db.Integer, db.Foreignkey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id
    
    def __repr__(self):
        return "<Post %r>" % self.id
    
class Follow(db.Model):
    __tablename__ = "follow"
    id = db.column(db.Integer, primary_key = True)
    user_id = db.column(db.Integer, db.Foreignkey('users.id'))
    follower_id = db.column(db.Integer, db.Foreignkey('users.id'))

    user = db.relationship('User', foreign_keys = user_id)
    follower = db.relationship('User', foreign_keys = follower_id)

    def __init__(self, user_id, follower_id):
        self.user_id = user_id
        self.follower_id = follower_id
    
    