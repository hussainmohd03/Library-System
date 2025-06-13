from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask import redirect, url_for
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key_here"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///library_system.db"
app.config["UPLOAD_FOLDER"] = "static/files"


db = SQLAlchemy(app)
login_manager = LoginManager(app)
Bootstrap5(app)


from . import routes, models, forms, admin, utils

def create_app():
    with app.app_context():
        db.create_all()
    return app


@login_manager.user_loader
def load_user(user_id):
    return models.User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))

