from flask import Flask
from models import db
from flask_cors import CORS



def create_app():
    app = Flask(__name__)
    app.secret_key = ''
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    CORS(app, 
        supports_credentials=True,
        origins=['http://localhost:3000'],
        allow_headers=["Content-Type"],
        expose_headers=["Set-Cookie"],
        methods=["GET", "POST", "OPTIONS", "DELETE"])

    with app.app_context():
        db.create_all()


    from routes import auth_routes, article_routes
    app.register_blueprint(auth_routes.bp)
    app.register_blueprint(article_routes.bp)


    return app
