from flask import Blueprint, render_template

from models import data

main = Blueprint("main", __name__)


@main.route("/")
def index():
    memo_list = data.get_all_memo_data()
    return render_template("index.html", memo_list=memo_list)


@main.route("/user/<name>")
def user(name=None):
    return render_template("user.html", name=name)
