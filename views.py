from flask import Flask

app = Flask(__name__)


app.route('/index')
def index():
        return 'hello world!'

app.route('/login')
def login():
    return 'login page'

if __name__ = '__main__':
    app.run()
