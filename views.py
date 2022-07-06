from app import db
from models import students,User
from werkzeug.security import generate_password_hash

def store_student(request_data):
    student = students(
        name=request_data["name"],
        city=request_data["city"],
        pin=request_data['pin'],
        addr=request_data["addr"],
    )
    db.session.add(student)
    db.session.commit()
    return student




def store_user(request_data):
    user = User(
        first_name = request_data["first_name"],
        last_name = request_data["last_name"],
        contact_number = request_data["contact_number"],
        email=request_data["email"],
        password=generate_password_hash(request_data["password"]),
    )
    db.session.add(user)
    db.session.commit()
    return user