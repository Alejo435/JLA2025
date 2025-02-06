import os
from flask import Flask
from app import app
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'coraldb.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Admins(db.Model):
    id = db.Column('admin_id', db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True, nullable = False)
    message = db.Column(db.String(500), unique = True, nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True, nullable = False)
    message = db.Column(db.String(500), unique = True, nullable = False)


    def __repr__(self):
        return '<Name %r>' % self.name
    

with app.app_context():
    db.drop_all()
    db.create_all()

    Ale = Students(name = "Alejandro Otermin", message = "Hi everyone, we'll be holding math tutoring after school in the gymtoday!")
    Yanis = Students(name = "Yanis Fellache", message = "Reminder basketball practice is today at 5:00")
    Stern = Admins(name = "Josh Stern", message = "Hey guys, reember the programming plans are due next Monday")
    Behar = Admins(name = "Marisa Behar", message = "Free snacks at programming comp today!")
    db.session.add(Ale)
    db.session.add(Yanis)
    db.session.add(Stern)
    db.session.add(Behar)
    db.session.commit()

