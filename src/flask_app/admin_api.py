from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
import datetime
from flask import current_app as app

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()

# Declaring the model.
class Book(db.Model):
    __tablename__ = "Book"
    BookID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Title = db.Column(db.Text)
    Author = db.Column(db.Text)
    PublishedDate = db.Column(db.DATE(), nullable=False)

    def __init__(self, Title, Author, BookID = None):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.PublishedDate = PublishedDate

class BookSchema(ma.Schema):
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        fields = ("BookID", "Title", "Author", "PublishedDate")

bookSchema = BookSchema()
booksSchema = BookSchema(many = True)

@api.route("/book", methods = ["GET"])
def getBooks():
    book = Book.query.all()
    result = booksSchema.dump(book)

    return jsonify(result.data)

@api.route("/book/<id>", methods = ["GET"])
def getBook(id):
    book = Book.query.get(id)

    return bookSchema.jsonify(book)

@api.route("/book", methods = ["POST"])
def addBook():
    title = request.json["title"]
    author = request.json["author"]
    PublishedDate = request.json["PublishedDate"]


    newBook = Book(Title = title, Author = author, PublishedDate = PublishedDate)

    db.session.add(newBook)
    db.session.commit()

    return bookSchema.jsonify(newBook)

@api.route("/book/<id>", methods = ["PUT"])
def bookUpdate(id):
    book = Book.query.get(id)
    title = request.json["title"]
    author = request.json["author"]
    PublishedDate = request.json["date"]

    book.Title = title
    book.Author = author
    book.PublishedDate = date

    db.session.commit()

    return bookSchema.jsonify(book)

@api.route("/book/<id>", methods = ["DELETE"])
def bookDelete(id):
    book = Book.query.get(id)

    db.session.delete(book)
    db.session.commit()

    return bookSchema.jsonify(book)
