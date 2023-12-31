from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    name = request.args.get('name')
    return 'Hello, {}'.format(name)


if __name__ == '__main__':
    app.run()