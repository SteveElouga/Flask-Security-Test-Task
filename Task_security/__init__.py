from flask import jsonify
from .extensions import db, jwt, app
from .views import views_bp
from .auth import auth_bp
from .user import users_bp
from .models import User

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(views_bp, url_prefix = "/view")
app.register_blueprint(auth_bp, url_prefix = "/auth")
app.register_blueprint(users_bp, url_prefix = "/users")

#Automatic loader

@jwt.user_lookup_loader
def user_lookup_callback(jwt_header, jwt_data):
    identity = jwt_data["sub"]
    
    return User.query.filter_by(email = identity).one_or_none()

#additional claims

@jwt.additional_claims_loader
def make_additional_claims(identity):
    
    if identity == "nyobeelouga5@gmail.com":
        return {"is_admin" : True}
    
    return {"is_admin" : False}
    


#jwt error handlers

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message":"Token has expired", "error":"token_expired"}), 401

@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"message":"Signature validation failed", "error":"invalid_token"}), 401

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"message":"Request does'nt contain a valid token", "error":"authorization_header"}), 401
    



