from app import db,app
from functools import wraps
from flask import request,jsonify,make_response
import jwt
from models import User


def token_required(f):
    @wraps(f)
    def decorator(*args , **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
            print(token,",,,,,,,,,,,,,,,,,,,,,,,,,,")
            

        if not token:
            return jsonify({'message': 'a valid token is missing'})
        
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'],  algorithms=["HS256"])
            print(data,"::::::::::::::::::::")
            current_user = User.query.filter_by(id=data['id']).first()
        except Exception as e:
            return make_response(jsonify({"message":str(e)}), 401)
        return f(*args, **kwargs)
    return decorator