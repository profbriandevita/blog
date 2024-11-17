from flask import jsonify, session
from models.user import User 
from models import db 


def register_user(data):
    if User.query.filter_by(email=data['email']).first() is not None:
        return jsonify({
            'error': 'El email ya esta registrado'
        }), 400
    
    new_user = User(username=data['username'], email=data['email'])
    new_user.set_password(data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({
        'message': f'Usuario {new_user.username} registrado con exito'
    }), 201

def login_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if user and user.check_password(data['password']):
        session['user_id'] = user.id
        
        return jsonify({'message': 'Inicio de sesion exitoso'}), 200
    else:
        return jsonify({'error': 'Credenciales invalidas'}), 401
    
def logout_user():
    session.pop('user_id', None)
    return jsonify({'message':'Sesion cerrada con exito'})