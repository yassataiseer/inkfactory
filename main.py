from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from query import data_answer
from user_fetcher import static
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

@app.route("/logger",methods = ["POST"])
def check():
    email = request.form['emailer']
    password = request.form['pswrd']
    variable = email,password
    variable = list(variable)
    boolean = data_answer.data(variable)
    if boolean == True:
        user_data = static.data()
        return render_template("users.html",user_data=user_data)
    else:
        return "invalid creds"


@app.route("/users")
def users():
    user_data = static.data()
    return render_template("users.html", user_data=user_data)

if __name__ == '__main__':
    app.run(debug=True)