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
    user["points"] = database_functions.getUserPoints(username, df)
    user["friends"] = database_functions.getUserFriends(username, df)


@app.route("/", methods=["GET", "POST"])
def index():
    if user == {}:
        return redirect(url_for("login"))
    if request.method == "POST":
        add = request.form.get("step_input")
        user["points"] += int(add)

    arr = ["Bronze", "Silver", "Gold", "Diamond", "Emerald"]
    t1 = int(user["points"] / 100)
    t2 = int(user["points"] % 100)

    path = [180, 150, 120, 100, 80, 50, 20, 0, 200, -50]  # of length 10
    coords = {'mapid': t1, 'indexid': path[int(t2 / 10)]}
    return render_template("index.html", points=user["points"], league=arr[t1], prog=t2, coords=coords)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        initialize_user(username)

        return redirect(url_for("index"))
    return render_template("login.html")


@app.route("/create", methods=["GET", "POST"])
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
