from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

### App configuration

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///strike.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "bvjchsygvduycgsyugc"

### ORM

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

### Login manager

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

from strike_app.auth.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

### Register blueprints

from strike_app.strike.views import strike_blueprint
app.register_blueprint(strike_blueprint, url_prefix="/staking")

from strike_app.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')