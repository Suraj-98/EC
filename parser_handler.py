from flask_restful import reqparse

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('name', location='form')
parser.add_argument('city', location='form')
parser.add_argument('pin', location='form')
parser.add_argument('addr', location='form')

user_parser = reqparse.RequestParser(bundle_errors=True)
user_parser.add_argument('first_name', location='form')
user_parser.add_argument('last_name', location='form')
user_parser.add_argument('contact_number', location='form')
user_parser.add_argument('email', location='form')
user_parser.add_argument('password', location='form')