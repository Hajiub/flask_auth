from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from .config import  DevelopmentConfig
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    login_manager.init_app(app)
    db.init_app(app)
    migrate = Migrate(app, db)

    @login_manager.user_loader
    def load_user(user_id):
        from .models import User
        return User.get(int(user_id))
    #register your blueprint
    from .auth import auth
    app.register_blueprint(auth)
    
    return app
