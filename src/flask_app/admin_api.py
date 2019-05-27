"""
admin_apy.py
=============
Admin Book API class
"""

from flask import Flask, Blueprint, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os, requests, json
from flask import current_app as app

api = Blueprint("api", __name__)

db = SQLAlchemy()
ma = Marshmallow()

class Book(db.Model):
    """
    The Admin Book API class
    This class maps objects to Database 
    while also providing endpoints for the flask
    app. 
    Params
        :MODEL: class which model is based
    """
    __tablename__ = "Book"
    BookID = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Title = db.Column(db.Text)
    Author = db.Column(db.Text)
    PublishedDate = db.Column(db.Date)

    def __init__(self, Title, Author, PublishedDate, BookID = None):
        self.BookID = BookID
        self.Title = Title
        self.Author = Author
        self.PublishedDate = PublishedDate

class BookSchema(ma.Schema):
    def __init__(self, strict = True, **kwargs):
        super().__init__(strict = strict, **kwargs)
    
    class Meta:
        # Fields to expose.
        fields = ("BookID", "Title", "Author", "PublishedDate")

bookSchema = BookSchema()
booksSchema = BookSchema(many = True)

@api.route("/book", methods = ["GET"])
def getBooks():
    """
    returns a json representation of the books schema
    """
    books = Book.query.all()
    result = booksSchema.dump(books)

    return jsonify(result.data)

@api.route("/book/<id>", methods = ["GET"])
def getBook(id):
    """
    returns a json representation of one book
    searches by BookID index
    """
    book = Book.query.get(id)

    return bookSchema.jsonify(book)

@api.route("/book", methods = ["POST"])
def addBook():
    """
    provides an endpoint for the creation of a new book
    requires fields title, author & publisheddate be populated
    and commits to the google cloud db
    """
    title = request.json["title"]
    author = request.json["author"]
    publisheddate = request.json["publisheddate"]

    newBook = Book(Title = title, Author = author, publisheddate = publisheddate)

    db.session.add(newBook)
    db.session.commit()

    return bookSchema.jsonify(newBook)

# Endpoint to update book.
@api.route("/book/<id>", methods = ["PUT"])
def bookUpdate(id):
    """
    provides an endpoint for admin 
    to search a book by its id and 
    update it accordingly
    """
    book = Book.query.get(id)
    title = request.json["title"]
    author = request.json["author"]
    publisheddate = request.json["publisheddate"]

    book.Title = title
    book.Author = author
    book.PublishedDate = publisheddate

    db.session.commit()

    return bookSchema.jsonify(book)

# Endpoint to delete book.
@api.route("/book/<id>", methods = ["DELETE"])
def bookDelete(id):
    book = Book.query.get(id)

    db.session.delete(book)
    db.session.commit()

    return bookSchema.jsonify(book)
