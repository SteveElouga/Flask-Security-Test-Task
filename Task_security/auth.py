from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, current_user, jwt_required, get_jwt
from .models import User

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/register")
def create_user():
    
    data = request.get_json()
    
    user = User.get_user_by_email(email=data.get("email"))
    
    if user is not None:
        return jsonify({"message":"User already exist!"}), 200
    
    new_user = User(
        first_name = data.get("first_name"),
        last_name = data.get("last_name"),
        email = data.get("email")
    )
    
    new_user.set_password(password=data.get("password"))
    new_user.save()
    
    return jsonify({"message":"User has created!"}), 201


@auth_bp.post("/login")
def login():
    data = request.get_json()
    
    user = User.get_user_by_email(email=data.get("email"))
    
    if user:
        
        create_access = create_access_token(identity=user.email)
        refresh_acess = create_refresh_token(identity=user.email)
        
        return jsonify({
            "message":"Logged In",
            "tokens":{
                "access": create_access,
                "refresh": refresh_acess
            }
        }), 200
        
    return jsonify({"message":"email or password incorrect!"})

@auth_bp.get("/whoami")
@jwt_required()
def whoami():
    return jsonify({"message": "message", "user_detail":{
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "email": current_user.email
    }})