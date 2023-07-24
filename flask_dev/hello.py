from flask import Flask
app = Flask(__name__)


@app.route('/hello/<string:name>')
def hello(name):
    return '{}, Welcome To The Hello Page'.format(name)
if __name__ == "__main__":
    app.run()