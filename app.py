from flask import Flask, render_template, jsonify, url_for, request, redirect
from models import db, Admins, Students  

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coraldb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

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

@app.route('/schedule')
def schedule():
    return render_template('schedule/schedule.html')


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