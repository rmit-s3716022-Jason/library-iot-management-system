from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from admin_api import api, db
from admin_site import site
from flask_bootstrap import Bootstrap

app = Flask(__name__)

bootstrap = Bootstrap(app)

basedir = os.path.abspath(os.path.dirname(__file__))

HOST = "localhost"
USER = "root"
PASSWORD = "amended"
DATABASE = "dbcloud"

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DATABASE)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db.init_app(app)

app.register_blueprint(api)
app.register_blueprint(site)

if __name__ == "__main__":
    app.run(host = "0.0.0.0")
