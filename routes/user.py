from flask import Blueprint, request, jsonify
from controllers.userController import get_all_users, create_user, edit_user, delete_user

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
    return create_user(name, email)

@user_bp.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    data=request.get_json()
    name=data.get('name')
    email=data.get('email')
    return edit_user(id, name, email)

@user_bp.route('/delete/<id>', methods=['DELETE'])
def delete(id):
    return delete_user(id)

