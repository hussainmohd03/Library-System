from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask import redirect, url_for


app = Flask(__name__)
app.config["SECRET_KEY"] = "6:3886&T£;Toz=c|m]@ku`j1>*"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Library.db'

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

