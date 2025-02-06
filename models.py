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
    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    question = db.Column(db.Text, nullable=True)  # Optional question
    filename = db.Column(db.String(255), nullable=True)  # Optional file upload
    comments = db.relationship("Comment", backref="post", cascade="all, delete-orphan")

    def __repr__(self):
        return f'<Post by {self.username}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    username = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Comment by {self.username}>'


