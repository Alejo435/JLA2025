import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'coraldb.sqlite3')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Admins(db.Model):
    id = db.Column('admin_id', db.Integer, primary_key = True)
    name = db.Column(db.String(150), unique = True, nullable = False)
    message = db.Column(db.String(300), unique = True, nullable = False)



    def __repr__(self):
        return '<Name %r>' % self.name

