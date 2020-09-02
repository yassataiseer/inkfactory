from flask import Flask, render_template,request,session
import json
import urllib.request
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("login.html")

if __name__ == '__main__':
    app.run(debug=True)