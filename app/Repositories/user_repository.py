from app.Models.user import User
from app.Models.role import Role
from app.Models.user_role import UserRole
from app import db


class UserRepository:
    @staticmethod
    def find_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username, password, role_names):
        if UserRepository.find_by_username(username):
            return None

        user = User(username=username, password=password)

        # Tambahkan role ke user
        for role_name in role_names:
            role = Role.query.filter_by(name=role_name).first()
            if not role:
                # Jika role tidak ada, buat role baru
                role = Role(name=role_name)
                db.session.add(role)
            user.roles.append(role)

        db.session.add(user)
        db.session.commit()
        return user