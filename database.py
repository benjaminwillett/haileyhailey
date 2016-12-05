from flask.ext.sqlalchemy import SQLAlchemy
import os
from flask import Flask

basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir is set to " + basedir)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
print(app.config)
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


db = SQLAlchemy(app)

class Devices(db.Model):
    __tablename__ = 'Devices'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    ports = db.Column(db.Integer, unique=True)
    vendor = db.Column(db.String(64), unique=True)
    print("Devices done")

    def __repr__(self):
        print("returned result")
        return  '<Devices %r>' % self.name


u = Devices(name='2TP-CSW-01', ports='1', vendor='Cisco')
db.session.add(u)
u = Devices(name='2TP-CSW-02', ports='4', vendor='Cisco')
db.session.add(u)
u = Devices(name='EB-CSW-01', ports='8', vendor='Cisco')
db.session.add(u)
u = Devices(name='EB-CSW-02', ports='3', vendor='Cisco')
db.session.add(u)
u = Devices(name='2TP-CSW-11', ports='48', vendor='HP')
db.session.add(u)
u = Devices(name='2TP-CSW-12', ports='28', vendor='HP')
db.session.add(u)
u = Devices(name='EB-CSW-11', ports='10', vendor='HP')
db.session.add(u)
u = Devices(name='EB-CSW-12', ports='38', vendor='HP')
db.session.add(u)
db.session.commit()
print(u)
print("Session committed")
queryAll = Devices.query.all()
print(queryAll)
# for e in u:
#     if (e.vendor == "HP"):
#         print(e.id,e.name,e.vendor)


class Users(db.Model):
    __tablename__ = 'Users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True)
    firstname = db.Column(db.String(64), unique=True)
    surname = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=True)
    age = db.Column(db.String(64), unique=True)
    gender = db.Column(db.String(64), unique=True)
    town = db.Column(db.String(64), unique=True)
    country = db.Column(db.String(64), unique=True)
    postcode = db.Column(db.String(64), unique=True)
    print("New User done")

    def __repr__(self):
        print("returned result")
        return  '<Users %r>' % self.name


class Routers(db.Model):
    __tablename__ = 'Routers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    ip = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64), unique=True)
    print("New Router done")

    def __repr__(self):
        print("returned result")
        return '<Routers %r>' % self.name
