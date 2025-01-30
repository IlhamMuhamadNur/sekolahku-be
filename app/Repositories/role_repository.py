from app.Models.role import Role
from app import db

class RoleRepository:
    @staticmethod
    def find_by_name(name):
        return Role.query.filter_by(name=name).first()

    @staticmethod
    def create_role(name):
        role = Role(name=name)
        db.session.add(role)
        db.session.commit()
        return role