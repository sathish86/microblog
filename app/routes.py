from app import app
from app.login import login

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/test')
def test():
    return "Test route url"

@app.route('/login')
def login():
    return "login page returned"
