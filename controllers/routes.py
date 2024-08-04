import os

from flask import Blueprint, render_template, request, redirect
from flask_login import UserMixin, LoginManager

from models import data

main = Blueprint("main", __name__)
main.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(run.app)

# メモデータ管理クラスのインスタンス生成
memo_db = data.MemoManager()


class User(UserMixin):
    def __init__(self, user_id) -> None:
        self.id = user_id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@main.route("/login", methods=["GET", "POST"])
def login():
    error_message = ""
    user_id = ""
    return render_template(
        "login.html", user_id=user_id, error_message=error_message
    )


@main.route("/")
def index():
    memo_list = memo_db.get_all_memo_data()
    return render_template("index.html", memo_list=memo_list)


@main.route("/user/<name>")
def user(name=None):
    return render_template("user.html", name=name)


# メモの登録してメモ一覧に戻る
@main.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        memo_db.insert_new_memo_data(title, body)
        return redirect("/")
    return render_template("regist.html")


# メモの編集してメモ一覧に戻る
@main.route("/<id>/edit", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        memo_db.edit_memo_data(id, title, body)
        return redirect("/")
    post = memo_db.get_memo_data(id)
    return render_template("edit.html", post=post[0])


# メモを削除してメモ一覧に戻る
@main.route("/<id>/delete", methods=["GET", "POST"])
def delete(id):
    if request.method == "POST":
        memo_db.delete_memo_data(id)
        return redirect("/")
    post = memo_db.get_memo_data(id)
    return render_template("delete.html", post=post[0])
