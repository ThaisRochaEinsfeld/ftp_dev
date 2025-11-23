from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    app.config['SECRET_KEY'] = 'dev'  
    
    db.init_app(app)

    from .routes.upload_routes import upload_bp
    from .routes.update_routes import update_bp
    from .routes.delete_routes import delete_bp
    from .routes.auth_routes import auth_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(upload_bp)
    app.register_blueprint(update_bp)
    app.register_blueprint(delete_bp)

    @app.route("/")
    def home():
        return redirect(url_for("auth.login"))

    with app.app_context():
        from .models.project import Project
        from .models.user import User
        db.create_all()

    return app
