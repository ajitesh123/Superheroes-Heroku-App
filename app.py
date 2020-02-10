import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Person
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
        heroes = Person.query.all()
        formatted_heroes = [hero.format() for hero in heroes]

        return jsonify({
            'result': formatted_heroes
        })


# ------------------------------------------------
# Error Handlers
# -------------------------------------------------





# -------------------------------------------------
    return app

app = create_app()

if __name__ == '__main__':
    app.run()
