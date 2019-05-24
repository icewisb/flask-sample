from flask import (
    abort, redirect,
    render_template,
    make_response,
    url_for,
    request,
    session,
    escape,
    Flask,
)

app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/index')
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session.get('username'))
    return 'You are not logged in'

    # resp = make_response(render_template('hello.html'))
    # resp.set_cookie('username', 'icew')
    # return resp
    # return redirect(url_for('login'))


@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return render_template('login.html')
    # if request.method == 'POST':
    #     return 'do login'
    # else:
    #     return 'show login form'


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('index')


@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return '{}\' profile'.format(username)


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'


# TODO: static file
# url_for('static', filename='style.css')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('uploaded_file.txt')


# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('page_not_found.html'), 404


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp
