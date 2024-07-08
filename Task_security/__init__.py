from .extensions import db, jwt, app
from .views import views_bp
from .auth import auth_bp
from .user import users_bp

db.init_app(app)
jwt.init_app(app)

app.register_blueprint(views_bp, url_prefix = "/view")
app.register_blueprint(auth_bp, url_prefix = "/auth")
app.register_blueprint(users_bp, url_prefix = "/users")



