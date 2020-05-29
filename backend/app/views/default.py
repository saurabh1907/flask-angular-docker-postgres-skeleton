from flask import render_template, redirect, jsonify, flash
from app import app
from app.forms import LoginForm

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

@app.route('/login' , methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)


# @app.route('/booksApi/', methods=['GET', 'PUT', 'DELETE'])
# def bookFunctionId(id):
#     if request.method == 'GET':
#         return get_book(id)
#
#     elif request.method == 'PUT':
#         title = request.args.get('title', '')
#         author = request.args.get('author', '')
#         genre = request.args.get('genre', '')
#         return updateBook(id, title, author, genre)
#
#     elif request.method == 'DELETE':
#         return deleteABook(id)