import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))


db = SQLAlchemy()

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
    

