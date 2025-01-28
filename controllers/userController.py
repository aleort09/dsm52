from models.user import User
from config import db
from flask import jsonify

def get_all_users():
    try:
        return [user.to_dict() for user in User.query.all()]
    except Exception as e:
        return jsonify(e)

def create_user(name, email):
    try:
        new_user = User(name, email)
        db.session.add(new_user)
        db.session.commit()
        return new_user.to_dict()
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"{e}"})


def edit_user(id, name, email):
    user=User.query.get(id)
    if not user:
        return jsonify({"error": "el usuario no existe"})
    
    user.name=name
    user.email=email
    try:
        db.session.commit()
        return jsonify({"message": "Usuario modificado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Error creando el usuario: {str(e)}"})

def delete_user(id):
    user=User.query.get(id)
    if not user:
        return jsonify({"error": "el usuario no existe"})
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"message": "Usuario eliminado"})
    except Exception as e:
        db.session.rollback()
        return jsonify({"error", f"Error eliminandoe l usuario: {str(e)}"})