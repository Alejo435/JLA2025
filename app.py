from flask import Flask, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/api/data', methods=['GET'])
def api_data():
    data = {"message": "Hello from the API!", "status": "success"}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)