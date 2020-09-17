from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from query import data_answer
from user_fetcher import static
from cli_fetcher import sheets
from generate import gather
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'prettyprinted'


@app.route("/")
def index():
    return render_template("login.html")



@app.route("/logger",methods = ["POST"])
def check():
    creds = request.form.get("name")
    #print(creds)
    email = request.form['emailer']
    session['email'] = email
    password = request.form['pswrd']
    variable = email,password
    variable = list(variable)
    boolean = data_answer.data(variable)#calls query.py class
    if boolean == True:
        user_data = static.data()
        if email=="taiseer142@hotmail.com":
            return render_template("users.html",user_data=user_data)
        else:
            return render_template("users.html",user_data=[["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["#"]])
    else:
        return "invalid creds"




@app.route("/users")
def users():
    if session['email'] == 'taiseer142@hotmail.com':
        user_data = static.data()#calls user_fetch.py class
        #print(user_data)
        creds = request.form.get("email")
        print("creds",creds)
        return render_template("users.html", user_data=user_data)
    else: 
        return render_template("users.html",user_data=[["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["#"]])


@app.route("/clients")
def clients():
    user_data = sheets.data()
    a = request.form.get('email')
    print(a)
    return render_template("clients.html", user_data=user_data)



@app.route("/change",methods = ['POST'])
def change():
    #print("Hello")
    creds = request.form.get("email")
    print(creds)
    if session['email'] !="taiseer142@hotmail.com":
        return"<h1> You don't have access to this only the master does :(</h1>"
    #print(creds)
    boolean = gather.data(creds)#calls on generate.py
    #print(boolean)
    passable = len(boolean)
    if passable>0:
        boolean = boolean[0]
        return render_template("change_user.html",user=boolean)
    else:
        return render_template("login.html")




@app.route("/rewrite",methods = ['POST'])
def rewrite():
    a = request.form['firstname']
    return render_template("users.html")


@app.route("/back")
def back():
    if session['email'] == 'taiseer142@hotmail.com':
        user_data = static.data()#calls user_fetch.py class
        #print(user_data)
        creds = request.form.get("email")
        print("creds",creds)
        return render_template("users.html", user_data=user_data)
    else: 
        return render_template("users.html",user_data=[["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["#"]])


if __name__ == '__main__':
    app.run(debug=True)