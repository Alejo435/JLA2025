from flask import Flask, render_template, jsonify, url_for, request, redirect

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
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in credentials and credentials[username] == password:
            logged_in = True
            return redirect(url_for('home'))
        else:
            return "Invalid credentials, please try again!", 401


    return render_template("login.html")


@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"message": "Hello from the API!", "status": "success"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)