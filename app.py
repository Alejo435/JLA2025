from flask import Flask, render_template, jsonify, url_for, request, redirect, send_from_directory
from models import db, Admins, Students, Comment, Post
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coraldb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["UPLOAD_FOLDER"] = "uploads"

if not os.path.exists("uploads"):
    os.makedirs("uploads")

db.init_app(app)

current_user = ""
logged_in = False

credentials = {
    "admin": "password123",
    "user": "testpass"
}

@app.route('/')
def home():
    global logged_in
    if logged_in:
        return render_template('index.html')
    return redirect(url_for('login'))

@app.route('/login', methods=["GET", "POST"])
def login():
    global logged_in, current_user
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in credentials and credentials[username] == password:
            logged_in = True
            current_user = username
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials, please try again!"

    return render_template("login.html", error=error)

@app.route("/signup", methods=["GET", "POST"])
def signup():
    """Handles the signup functionality."""
    global credentials
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in credentials:
            return render_template("signup.html", error="Username already exists!")

        credentials[username] = password
        return redirect(url_for('login'))

    return render_template("signup.html")

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/schedule')
def schedule():
    return render_template('schedule/schedule.html')


@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/community')
def community():
    """Renders the community page where posts, questions, and file uploads are displayed."""
    posts = Post.query.all()  # Fetch all posts with questions & file uploads
    return render_template('community.html', posts=posts)


@app.route('/upload', methods=["POST", "GET"])
def upload_file():
    if request.method == "GET":
        return redirect(url_for("community"))
    """Handles file uploads and post creation."""
    username = current_user
    question = request.form.get("question")
    file = request.files.get("file")

    filename = None
    if file and file.filename:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

    # Ensure at least a question or file is provided
    if not question and not filename:
        return redirect(url_for("community"))

    new_post = Post(username=username, question=question, filename=filename)
    db.session.add(new_post)
    db.session.commit()

    return redirect(url_for("community"))


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    """Serves uploaded files."""
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)


@app.route('/comment/<int:post_id>', methods=["POST"])
def comment(post_id):
    """Handles comment submission for posts."""
    username = current_user
    text = request.form.get("text")

    new_comment = Comment(post_id=post_id, username=username, text=text)
    db.session.add(new_comment)
    db.session.commit()
    
    return redirect(url_for("community"))

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"message": "Hello from the API!", "status": "success"}
    return jsonify(data)

@app.route('/api/student_info', methods=['GET'])
def get_studentInfo():
    items = Students.query.all()  
    items_list = [{"name": item.name, "message": item.message} for item in items]
    return jsonify(items_list)

@app.route('/api/admin_info', methods=['GET'])
def get_adminInfo():
    items = Admins.query.all()  
    items_list = [{"name": item.name, "message": item.message} for item in items]
    return jsonify(items_list)


def create_db():
    with app.app_context():
        db.create_all()  
        if not Admins.query.first() and not Students.query.first():
            Ale = Students(name="Alejandro Otermin", message="Hi everyone, we'll be holding math tutoring after school in the gym today!")
            Yanis = Students(name="Yanis Fellache", message="Reminder: basketball practice is today at 5:00")
            Stern = Admins(name="Josh Stern", message="Hey guys, remember the programming plans are due next Monday")
            Behar = Admins(name="Marisa Behar", message="Free snacks at the programming comp today!")

            db.session.add_all([Ale, Yanis, Stern, Behar])
            db.session.commit()


if __name__ == '__main__':
    create_db() 
    print("Created DB") 
    app.run(debug=True)