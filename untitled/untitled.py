from flask import Flask, render_template
from requests import *

app = Flask(__name__)


@app.route('/index')
def hello_world():
    return render_template('index.html')

@app.route('/')
def contact():
    if request.method == 'POST':
        if request.form['submit'] == 'Do Something':
            pass # do something
        elif request.form['submit'] == 'Do Something Else':
            pass # do something else
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run()
