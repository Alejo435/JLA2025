from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy database object
db = SQLAlchemy()

# Define the Admins model
class Admins(db.Model):
    id = db.Column('admin_id', db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    message = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f'<Admin {self.name}>'

# Define the Students model
class Students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    message = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return f'<Student {self.name}>'


