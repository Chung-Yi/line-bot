from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        username = request.values['username']
        password = request.values['password']
        if username == 'david' and password == '1234':
            return 'Welcome to the page.'
        else:
            return 'your username or password is wrong.'
    return """
           <form method='post' action=''>
               <p>帳號:<input type='text' name='username' /></p>
               <p>密碼:<input type='text' name='password' /></p>
               <p><button type='submit'>確定</button></p>
            </form>
           """


if __name__ == '__main__':
    app.run()