from models.user import User
from config import db
from flask import jsonify

def get_all_users():
    users=User.query.all()
    return [user.to_dict() for user in users]

def create_user(name, email):
    if not all([name, email]):
        return jsonify({"error": "Los campos deben de estar llenos"}), 400
    
    new_user = User(name=name, email=email)
    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Usuario creado"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error creando el usuario: {str(e)}"}), 500