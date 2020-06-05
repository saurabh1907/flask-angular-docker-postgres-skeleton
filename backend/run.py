# Some tutorials call this file wsgi.py
from flask import jsonify
from app import create_app

app = create_app()  # App initialization


@app.route('/api')
def hello():
    return "Hello from Flask using Python. You might want to go to /api/blogs, /api/blogs/id"


@app.route("/api/health")
def health():
    return jsonify({"status": 200, "msg": "Flask backend is running!"})


if __name__ == '__main__':
    # app.run(debug=True)
    app.run()
