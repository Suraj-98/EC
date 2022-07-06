from app import app, api
from api import StudentList,Create_Student,Students,Create_User, LoginUser, UserList,Users

api.add_resource(StudentList, '/students')
api.add_resource(Create_Student, '/create')
api.add_resource(Students, '/student/<id>')
api.add_resource(Create_User, '/create_user')
api.add_resource(LoginUser, '/login')
api.add_resource(UserList, '/users')
api.add_resource(Users, '/user/<username>')