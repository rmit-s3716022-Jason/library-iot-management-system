from flask import Flask, Blueprint, request, jsonify, render_template, redirect
from flask import flash
from wtforms import TextField, DateField, validators
from flask_wtf import FlaskForm
from admin_form import BookForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json

site = Blueprint("site", __name__)

# Client webpage.
@site.route("/")
def index():
    # Use REST API.
    response = requests.get("http://127.0.0.1:5000/book")
    data = json.loads(response.text)

    return render_template("index.html", book = data)

@site.route("/form", methods=['GET', 'POST'])
def add_form():

    form = BookForm()
    if form.is_submitted():
        result = request.form
        title = request.form['title']
        author = request.form['author']
        publisheddate = request.form['publisheddate']

        data = {
            "title": title,
            "author": author,
            "publisheddate" : publisheddate
        }

        headers = {
            "Content-type": "application/json"
        }

        response = requests.post("http://127.0.0.1:5000/book", data = json.dumps(data), headers = headers)
        data1 = json.loads(response.text)

        return render_template("book.html", result=result)
    return render_template("form.html", form=form)

@site.route("/BookAdd", methods=['GET'])
def add_book():

    return render_template("add.html")

@site.route("/BookEdit")
def edit_book():
    pass

@site.route("/BookDelete", methods=['GET'])
def delete_book():

    BookID = request.form("BookID")
    
    url = "http://127.0.0.1:5000/book/<>"

    headers = {
            "Content-type": "application/json"
    }

    response = requests.delete(url, headers=headers, BookID=BookID)

    print(response.text)

    return render_template("delete.html")

@site.route("/AdminGraph")
def admin_graph():
    
    return render_template("graph.html")


@site.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember.data))
        if form.username.data == 'jaqen' and form.remember.data == 'hghar':
            return redirect('/index.html')
        else:
            return redirect('/login')
    return render_template('login.html', title='Sign In', form=form)

@site.route("/AdminLogout")
def logout_admin():
    pass

