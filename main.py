from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
from query import data_answer
from user_fetcher import static#grabs data of all users to be displayed on  users.html
from cli_fetcher import sheets#grabs client data from clients.db
from generate import gather#gathers specific employees data
import random
from email_checker import find#checks if they email is Admins
from db_rewriter import table_edit#rewrites employees data

from clients_data_finder import search# gathers the data of the specific client

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'


@app.route("/")
def index():
    session['email'] = None
    return render_template("login.html")


@app.route("/sign_out")
def sign_out():
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
    print("EMAIL",creds)
    captcha = find.search(session['email'])
    if  captcha!=True:
        return"<h1> You don't have access to this only the master does :(</h1>"
    boolean = gather.data(creds)#calls on generate.py
    passable = len(boolean)
    if passable>0:
        boolean = boolean[0]
        return render_template("change_user.html",user=boolean)
    else:
        return render_template("login.html")




@app.route("/rewrite",methods = ['GET'])
def rewrite():
    if request.method=="GET":
        first_name = request.args.get('firstname',None)
        print(first_name)
        last_name = request.args.get('lastname')
        email = request.args.get("mail")
        password = request.args.get('password')
        newdate=request.args.get('date')
        table_edit.write(first_name,last_name,email,password,newdate)
        user_data = static.data()#calls user_fetch.py class
        return render_template("users.html", user_data=user_data)


@app.route("/back" ,methods = ['GET','POST'])
def back():
    captcha = find.search(session['email'])#calls email_checker.py
    if captcha == True:
        user_data = static.data()#calls user_fetch.py class
        #print(user_data)
        return render_template("users.html", user_data=user_data)
    else: 
        return render_template("users.html",user_data=[["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["#"]])

@app.route("/change_clients",methods = ['POST'] )
def change_clients():
    if request.method=="POST":
        name = request.form.get("edit")
        #print(name)
        user_data = search.data(name)
        for user in user_data:
            print(user[0])
        return render_template("change_client.html",user_data = user_data)
    else:
        return"error"


if __name__ == '__main__':
    app.run(debug=True)