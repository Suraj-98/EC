from flask_restful import Resource
from app import db,app
from parser_handler import parser,user_parser
from views import store_student,store_user
from flask import request,jsonify,make_response
import jwt
import datetime
from werkzeug.security import check_password_hash
from deco import token_required
from models import students, User

class Students(Resource):

    @token_required
    def get(self, id):
        student = db.session.query(students).filter_by(id=id).first()
        data = {
            "name": student.name,
            "city": student.city,
            "pin": student.pin,
            "addr": student.addr
        }
        print(data)
        return data

    @token_required
    def delete(self, id):
        student = db.session.query(students).filter_by(id=id).delete()
        print(student, ">>>>>>>>>>>")
        db.session.commit()
        return {"status": True, "message": "student deleted successfully"}

class StudentList(Resource):

    @token_required
    def get(self):
        all_students = []
        student = db.session.query(students).all()
        for user in student:
            data = {
                "name": user.name,
                "city": user.city,
                "pin": user.pin,
                "addr": user.addr
            }
            all_students.append(data)
        print(all_students, ">>>>>>>>>>>.")
        return {"status": True, "data": all_students}

class Create_Student(Resource):

    @token_required
    def post(self):
        data = parser.parse_args()
        data1 = store_student(data)
        return {"status": True, "data": data, "message": "student account created successfully"}
    

class Create_User(Resource):

    def post(self):
        data = user_parser.parse_args()
        data1 = store_user(data)
        return {"status": True, "data": data, "message": "user account created successfully"}


class LoginUser(Resource):
    
    def post(self):

        auth = request.authorization
        print(auth, "$$$$$$$$$$$$")

        if not auth or not auth.username or not auth.password:
            return make_response('could not verify >>>', 401, {'WWW.Authentication': 'Basic realm: "login required"'})

        user = db.session.query(User).filter_by(email=auth.username).first()
        print(user, ">>>>>>>>>>>>")

        if check_password_hash(user.password,auth.password):
            token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=10)}, app.config['SECRET_KEY'])
 
            print("token =",token)
            return make_response(jsonify({"status": True, 'token': token}),200)



        return make_response('could not verify',  401, {'WWW.Authentication': 'Basic realm: "login required"'})

class UserList(Resource):

    @token_required
    def get(self):
        all_users = []
        user = db.session.query(User).all()
        for user in user:
            data = {
                "username": user.username,
            }
            all_users.append(data)
        print(all_users, ">>>>>>>>>>>.")
        return {"status": True, "data": all_users}

class Users(Resource):

    @token_required
    def get(self,username):

        user=db.session.query(User).filter_by(username=username).first()
        data ={
            "username":user.username
            }
        return {"status":True, "data":data}