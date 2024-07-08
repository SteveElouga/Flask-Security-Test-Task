from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt
from .models import User
from .schemas import User_schema

users_bp = Blueprint("users", __name__)

@users_bp.get("/all")
@jwt_required()
def get_all_users():
    
    claims = get_jwt()
    
    if claims.get("is_admin") == True:

        page = request.args.get('page', default=1, type=int)
        per_page = request.args.get('per_page', default=3, type=int)

        users = User.query.paginate(
            page=page,
            per_page=per_page
        )
        
        result = User_schema().dump(users, many=True)
        
        return jsonify({
            "users":result
        })
        
    return jsonify({"message": "you are'nt authorize to access to this"}), 403