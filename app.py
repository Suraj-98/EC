from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = '004f2af45d3a4e161a7dd2d17fdae47f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users\Dell\Desktop\EC\e-commerce\students.sqlite3'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aviox:suraj123@localhost/data'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False