from flask import Blueprint, render_template, request, redirect

from models import data

main = Blueprint("main", __name__)

# メモデータ管理クラスのインスタンス生成
memo_db = data.MemoManager()


@main.route("/")
def index():
    memo_list = memo_db.get_all_memo_data()
    return render_template("index.html", memo_list=memo_list)


@main.route("/user/<name>")
def user(name=None):
    return render_template("user.html", name=name)


@main.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        memo_db.insert_new_memo_data(title, body)
        return redirect("/")
    return render_template("regist.html")
