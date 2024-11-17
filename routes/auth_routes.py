from flask import Blueprint, request, jsonify, session
from models import User
from services.auth_service import register_user, login_user



bp = Blueprint('auth', __name__)


@bp.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    return register_user(data)
   

@bp.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    return login_user(data)
   

@bp.route('/logout', methods=['POST'])
def logout_user_route():
    return logout_user_route()


@bp.route('/check-auth', methods=['GET'])
def check_auth_route():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.get(user_id)
        if user:
            return jsonify({
                'authenticated': True,
                'username': user.username,
                'user_id': user.id
            }), 200
        else:
            return jsonify({
                'authenticated': False,

            }),401
    else:
        return jsonify({
                'authenticated': False,

            }),401
