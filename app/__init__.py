from flask import (
    Flask,
    render_template,
    jsonify,
    send_from_directory,
    request,
    redirect,
    url_for,
)
from . import database_functions

app = Flask(__name__)
df = database_functions.createSampleDataframe()
user = {}


def initialize_user(username):
    user["username"] = username
    user["points"] = getUserPoints(username, df)
    user["friends"] = getFriends(username, df)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login")
def login():
    if request.method == "POST":
        username = request.form.get("username")

        if not database_functions.checkUser(username, df):
            return redirect(url_for("login"))

        initialize_user(username)

    return render_template("login.html")


@app.route("/create")
def create():
    if request.method == "POST":
        username = request.form.get("username")

        if username == None:
            return redirect(url_for("create"))

        if adduser(username, df) == None:
            return redirect(url_for("create"))

        initialize_user(username)

    return render_template("create.html")


@app.route("/group")
def group():
    # if user == {}:
    # return redirect(url_for("login"))

    return render_template("group.html")  # , group=user["friends"])
