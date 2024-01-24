import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

def is_on_github_actions():
    if "CI" not in os.environ or not os.environ["CI"] or "GITHUB_RUN_ID" not in os.environ:
        return False
    else:
        return True

# Database Setup
app = Flask(__name__)

app.config['SECRET_KEY'] = 'supersecret' # To allow us to use forms
app.config["TEMPLATES_AUTO_RELOAD"] = True

basedir = os.path.abspath(os.path.dirname(__file__))
password = "password123"

if is_on_github_actions():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql://admin:{password}@tbo-mysql/tbo"

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)


# Register Blueprints
from project.core.views import core
from project.books.views import books
from project.customers.views import customers
from project.loans.views import loans

app.register_blueprint(core)
app.register_blueprint(books)
app.register_blueprint(customers)
app.register_blueprint(loans)