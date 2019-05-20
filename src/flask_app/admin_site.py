from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_wtf import FlaskForm
from admin_form import LoginForm
import os, requests, json


site = Blueprint("site", __name__)

@site.route("/")
@site.route("/home")
def index():
    return render_template("index.html")

@site.route("/login")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Sign In', form=form)

@site.route("/search")
def book_search():
    
    
    response = requests.get("http://127.0.0.1:5000/book")
    return render_template("book_search.html")

@site.route("/create")
def book_borrow():
    

    return render_template("book_borrow")

@site.route("/return")
def book_return():

    return render_template("book_return")
