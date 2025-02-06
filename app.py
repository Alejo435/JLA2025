from flask import Flask, render_template, jsonify, url_for, request, redirect
from database import db, Admins, Students

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coraldb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

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
    global logged_in
    error = None
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in credentials and credentials[username] == password:
            logged_in = True
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials, please try again!"


    return render_template("login.html", error=error)


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"message": "Hello from the API!", "status": "success"}
    return jsonify(data)

@app.route('/api/student_info', methods=['GET'])
def get_studentInfo():
    items = Students.query.all()  
    items_list = [{"id": item.student_id, "name": item.name, "message": item.message} for item in items]
    print(items_list)
    return jsonify(items_list)
    

if __name__ == '__main__':
    app.run(debug=True)