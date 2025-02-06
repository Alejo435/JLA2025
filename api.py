from flask import Flask, request, jsonify, render_template, Response, redirect, url_for

app = Flask(__name__)
web = Flask(__name__, template_folder='Templates')

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run()

@web.route('/admin')
def index():
    return render_template('index.html')