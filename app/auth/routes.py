from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models import User
from app import db
from app.schemas import UserSchema

user_schema = UserSchema()

class Login(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = self.parser.parse_args()
        user = User.query.filter_by(username=data['username']).first()
        if not user or not user.verify_password(data['password']):
            return {'error': 'Invalid credentials'}, 401

        access_token = create_access_token(identity=user.id)
        return {'access_token': access_token}, 200

class Signup(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, help='Username is required')
        self.parser.add_argument('password', type=str, required=True, help='Password is required')

    def post(self):
        data = self.parser.parse_args()
        existing_user = User.query.filter_by(username=data['username']).first()
        if existing_user:
            return {'error': 'Username already exists'}, 400

        user = User(username=data['username'])
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()
        return user_schema.dump(user), 201
