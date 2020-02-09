import os
from flask import Flask
from models import setup_db
from flask_cors import CORS
from flask_migrate import Migrate, MigrateCommand


def create_app(test_config=None):


# ------------------------------------------------
# App Configuration
# -------------------------------------------------
    app = Flask(__name__)
    setup_db(app)
    CORS(app)


# ------------------------------------------------
# Controllers
# -------------------------------------------------
    @app.route('/')
    def get_greeting():
        excited = os.environ['EXCITED']
        greeting = "Hello"
        if excited == 'true': greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"


# ------------------------------------------------
# Error Handlers
# -------------------------------------------------





# -------------------------------------------------
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
