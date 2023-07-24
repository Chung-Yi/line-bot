from flask import Flask
from flask import render_template
from datetime import datetime


app = Flask(__name__)

@app.route('/hello/<string:name>')
def hello(name):
    now = datetime.now()
    return render_template('hello3.html', **locals())


if __name__ == '__main__':
    app.run()