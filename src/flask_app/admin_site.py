from flask import Flask, Blueprint, request, jsonify, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from admin_login import LoginForm
import os, requests, json

site = Blueprint("site", __name__)

@site.route("/")
@site.route("/index")
def index():

    return render_template("index.html")

@site.route("/login", methods=['GET', 'POST'])
@site.route("/index.html")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember.data))
        return redirect('/dashboard')
    return render_template('login.html', title='Sign In', form=form)

@site.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')


@site.route("/add", methods=['POST'])
def add():
    api = admin_api()
    title = request.form['Title']
    author = request.form['Author']
    date_published = request.form['Date_published']

    data = {
        "Title": title,
        "Author": author, 
        "PublishedDate": date_published
    }

    headers = {
        "content-type": "application/json"
    }

    response = requests.post("http://127.0.0.1:5000/book", data= json.dumps(data), headers=headers)
    data = json.loads(response.text)
    
    return render_template("dashboard.html", data=data, title=title, author=author, date_published=date_published)

@site.route("/edit")
def edit():
    pass

@site.route("/remove")
def remove():
    pass

@site.route("/logout")
def logout():
    pass

