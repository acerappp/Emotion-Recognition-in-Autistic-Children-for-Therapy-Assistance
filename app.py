# -- PENTING! REMOVE all monkey_patch/gevent/eventlet imports --
from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from emotion_recognition import db
from emotion_recognition.models import User, Patient, Session, EmotionalData
from emotion_recognition.routes import routes

app = Flask(__name__, template_folder='emotion_recognition/templates')
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/asyra/Desktop/application/emotion_recognition/database/fyp_system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'routes.login'

app.register_blueprint(routes)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == "__main__":
    app.run(port=5000, debug=True)
