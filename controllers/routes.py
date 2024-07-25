from flask import Blueprint, render_template

from models import data

main = Blueprint("main", __name__)


@main.route("/")
def index():
    return render_template("index.html", memo_list=data.memo_list)


@main.route("/user/<name>")
def user(name=None):
    return render_template("user.html", name=name)
