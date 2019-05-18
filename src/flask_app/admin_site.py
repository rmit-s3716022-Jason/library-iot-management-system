from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

site = Blueprint("site", __name__)

@site.route("/")
def index():
    response = requests.get("http://127.0.0.1:5000/book")
    data = json.loads(response.text)

    return render_template("index.html", book = data)
