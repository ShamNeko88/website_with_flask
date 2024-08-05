import os

from flask import Flask, redirect
from flask_login import LoginManager
from controllers.routes import main, User

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.register_blueprint(main)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    return redirect("/login")


if __name__ == '__main__':
    app.run(debug=True)
