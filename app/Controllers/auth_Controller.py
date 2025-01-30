from flask import request, jsonify
from app.services.Auth_service import AuthService

class AuthController:
    @staticmethod
    def register():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        roles = data.get('roles', [])

        if not roles:
            return jsonify({"message": "Roles are required"}), 400

        user = AuthService.register(username, password, roles)
        if user:
            return jsonify({"message": "User registered successfully"}), 201
        return jsonify({"message": "User already exists"}), 400

    @staticmethod
    def login():
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        token = AuthService.login(username, password)
        if token:
            return jsonify({"token": token},{"message" : "hai {{'username'}}"}), 200
        return jsonify({"message": "pw atau un salah"}), 401