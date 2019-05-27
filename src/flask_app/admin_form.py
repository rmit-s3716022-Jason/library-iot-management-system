from wtforms import Form, TextField, DateField, StringField, BooleanField, SubmitField, PasswordField, validators
from flask_wtf import FlaskForm

class BookForm(FlaskForm):
    title = TextField("Title", [validators.DataRequired("Requires a title")])
    author = TextField("Author", [validators.DataRequired("Requires author's name")])
    publisheddate = DateField("Date", [validators.data_required("Requires the date the book was published")], format='%Y-%m-%d')

class LoginForm(FlaskForm):
    username = StringField('Username', [validators.DataRequired("Requires")])
    password = PasswordField('Password', [validators.DataRequired("Requires")])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
