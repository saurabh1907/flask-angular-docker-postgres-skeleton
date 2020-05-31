from flask import render_template, jsonify
from app import app

@app.route('/api')
def hello():
    return "Hello from Flask using Python"

@app.route("/api/health")
def health():
    return jsonify({"status": 200, "msg":"Flask backend is running!"})

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)