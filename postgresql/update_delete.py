from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:123456@127.0.0.1:5433/testdb'
db = SQLAlchemy(app)

class students(db.Model):
    __tabelname__ = 'students'
    sid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    tel = db.Column(db.String(50))
    addr = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, tel, addr, email):
        self.name = name
        self.tel = tel
        self.addr = addr
        self.email = email

@app.route('/updateusr/<int:uid>')
def updateusr(uid):
    student = students.query.get(uid)
    student.name = student.name + '(已修改)'
    db.session.commit()
    return "資料修改成功"

@app.route('/deleteusr/<int:uid>')
def deleteusr(uid):
    student = students.query.get(uid)
    db.session.delete(student)
    db.session.commit()
    return "資料刪除成功"


if __name__ == '__main__':
    app.run()