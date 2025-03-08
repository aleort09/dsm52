from flask import Blueprint, request, jsonify
from controllers.userController import get_all_users, create_user, edit_user, delete_user, login_user

user_bp=Blueprint('users', __name__)

@user_bp.route('/', methods=['GET'])
def index():
    user = get_all_users()
    return jsonify(user)

@user_bp.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    new= create_user(name, email, password)
    return jsonify(new)

@user_bp.route('/edit/<id>', methods=['POST'])
def edit(id):
    data=request.get_json()
    name=data.get('name')
    email=data.get('email')
    return edit_user(id, name, email)

@user_bp.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    return delete_user(id)

@user_bp.route('/login', methods=['POST'])
def login():
    data=request.get_json()
    return login_user(data['email'], data['password'])
