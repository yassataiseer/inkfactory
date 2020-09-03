from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from query import data_answer
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
        return render_template("users.html")
    else:
        return "invalid creds"

if __name__ == '__main__':
    app.run(debug=True)