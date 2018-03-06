from flask import Flask, url_for, render_template
from jinja2 import Markup

app = Flask(__name__)

@app.template_filter('cap')
def capitalize(word):
    return word[0].upper() + word[1:]

@app.route('/')
def index():
    return '<html><body><h1>Ahoj!</h1></body></html>'

@app.route('/url/')
def url():
    return url_for('hello',
                   name='Petr',
                   count=123,
                   _external=True)

@app.route('/hello/')
@app.route('/hello/<name>/')
@app.route('/hello/<name>/<int:count>/')
def hello(name=None, count=1):
    return render_template(
        'hello.html',
        name=name)

# http://127.0.0.1:5000/hello/petr/300/
