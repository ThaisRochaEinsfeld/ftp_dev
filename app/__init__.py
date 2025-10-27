from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'dev'

    db.init_app(app)

    from .routes.upload_routes import upload_bp
    app.register_blueprint(upload_bp)

    with app.app_context():
        from .models.project import Project
        db.create_all()

    return app
