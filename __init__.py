from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/login")
def index():
    return render_template('login.html')

@app.route("/create")
def index():
    return render_template('create.html')

@app.route("/group")
def index():
    return render_template('group.html')
