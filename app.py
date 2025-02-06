from flask import Flask, render_template, jsonify, url_for, request, redirect
from db import db
from db import Admins, Students

app = Flask(__name__)

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
    items = Admins.query.all()  
    items_list = [{"id": item.student_id, "name": item.name, "message": item.message} for item in items]
    print(items_list)
    return jsonify(items_list)
    

if __name__ == '__main__':
    app.run(debug=True)