from flask import Flask, Blueprint, request, jsonify, render_template, redirect
from flask import flash
from wtforms import TextField, DateField, validators
from flask_wtf import FlaskForm
from admin_form import BookForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from datetime import datetime

class Book:
    def __init__(self, id, title, author, publisheddate):
        self.bookid = id
        self.author = author
        self.title = title
        self.publisheddate = publisheddate

site = Blueprint("site", __name__)

# Client webpage.
@site.route("/")
def index():
    # Use REST API.
    response = requests.get("http://127.0.0.1:5000/book")
    data = json.loads(response.text)

    return render_template("index.html", books=data)

@site.route("/BookAdd", methods=['GET', 'POST'])
def add_book():

    form = BookForm()
    if form.is_submitted():
        result = request.form
        title = request.form['title']
        author = request.form['author']
        publisheddate = request.form['publisheddate']

        data = {
            "title": title,
            "author": author,
            "publisheddate": publisheddate
        }

        headers = {
            "Content-type": "application/json"
        }

        response = requests.post("http://127.0.0.1:5000/book", data=json.dumps(data), headers=headers)
        response_data = json.loads(response.text)

        return render_template("book.html", result=response_data)
    return render_template("form.html", form=form)

@site.route("/BookEdit/<int:id>", methods=['GET', 'POST'])
def edit_book(id):
    if request.method == 'POST':
        form = BookForm()
        if form.validate():
            title = request.form['title']
            author = request.form['author']
            published_date = request.form['publisheddate']

            data = {
                "title": title,
                "author": author,
                "publisheddate": published_date
            }

            headers = {
                "Content-type": "application/json"
            }

            requests.put(
                "http://127.0.0.1:5000/book/{}".format(id),
                data=json.dumps(data),
                headers=headers)
            return redirect('/')

    response = requests.get("http://127.0.0.1:5000/book/{}".format(id))

    if not response:
        return 'Error loading book #{id}'.format(id=id)

    data = json.loads(response.text)

    book = Book(
        id, data['Title'],
        data['Author'], datetime.strptime(data['PublishedDate'], "%Y-%m-%d"))

    form = BookForm(formdata=data, obj=book)
    return render_template("edit_form.html", form=form, book_id=data['BookID'])

@site.route("/BookDelete/<int:id>", methods=['GET'])
def delete_book(id):

@site.route("/BookDelete", methods=['GET', 'POST'])
def delete_book():

    if request.method == 'POST':

        bookID = request.form.get("BookID")
    
        response = requests.delete("http://127.0.0.1:5000/book/" + bookID)
        print(response.text)

        return render_template("delete.html")
    else:
     return render_template("index.html")

@site.route("/AdminGraph")
def admin_graph():
    
    return render_template("graph.html")


@site.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.password.data))
        if form.username.data == 'jaqen' and form.password.data == 'hghar':
            return redirect('/')
        else:
            return redirect('/login')
    return render_template('login.html', title='Sign In', form=form)

@site.route("/AdminLogout")
def logout_admin():
    return render_template("index.html")

