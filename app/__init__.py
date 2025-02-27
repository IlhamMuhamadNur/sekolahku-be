from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)

    with app.app_context():
        from app.routes.route import auth_bp
        app.register_blueprint(auth_bp, url_prefix='/auth')

        db.create_all()

    return app