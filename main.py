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
from email_checker import find

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'


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
        print("kys")
        first_name = request.args.get('firstname',None)
        print(first_name)

        last_name = request.args.get('lastname')
        email = request.args.get("email")
        password = request.args.get('password')
        newdate=request.args.get('date')
        print(last_name)
        print(email)
        print(password)
        print(newdate)

        return render_template("users.html")


@app.route("/back" ,methods = ['GET','POST'])
def back():
    captcha = find.search(session['email'])#calls email_checker.py
    if captcha == True:

        user_data = static.data()#calls user_fetch.py class
        #print(user_data)
        
        return render_template("users.html", user_data=user_data)
    else: 
        return render_template("users.html",user_data=[["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["Your account does not have access"],["#"]])


if __name__ == '__main__':
    app.run(debug=True)