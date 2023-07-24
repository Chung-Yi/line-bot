from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome To The Main Page."

@app.route('/hello')
def hello():
    return "Welcome To The Hello Page."
if __name__ == '__main__':
    app.run()