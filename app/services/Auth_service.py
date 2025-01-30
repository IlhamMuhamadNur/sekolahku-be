from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app.Repositories.user_repository import UserRepository
from datetime import timedelta

class AuthService:
    @staticmethod
    def register(username, password, role_names):
        user = UserRepository.create_user(username, password, role_names)
        if user:
            return user
        return None

    @staticmethod
    def login(username, password):
        user = UserRepository.find_by_username(username)
        if user and user.password == password:
            roles = ''.join([role.name for role in user.roles])
            additional_claims = {"username": user.username, "roles": roles}
            access_token = create_access_token(identity=user.id, additional_claims=additional_claims, expires_delta=timedelta(hours=1))
            
            welcome_message = f"Selamat datang {roles} {user.username}!"
            return {"token": access_token, "message": welcome_message}
        return None