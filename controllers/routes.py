from flask import Blueprint, render_template, request, redirect
from flask_login import login_required, UserMixin, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from models import data

main = Blueprint("main", __name__)


# メモデータ管理クラスのインスタンス生成
memo_db = data.MemoManager()


# ログインユーザーのインスタンス
class User(UserMixin):
    def __init__(self, user_id) -> None:
        self.id = user_id


@main.route("/logout", methods=["GET"])
def logout():
    logout_user()
    return redirect("/login")


@main.route("/signup", methods=["GET", "POST"])
def signup():
    error_message = ""
    if request.method == "POST":
        id = request.form.get("user_id")
        password = request.form.get("password")
        if memo_db.get_user(id) != []:
            error_message = "既に存在するユーザーです"
        else:
            hashed_password = generate_password_hash(password)
            memo_db.insert_new_user(id, hashed_password)
            return redirect("/login")
    return render_template("signup.html", error_message=error_message)


@main.route("/login", methods=["GET", "POST"])
def login():
    error_message = ""
    user_id = ""

    if request.method == "POST":
        user_id = request.form.get("user_id")
        password = request.form.get("password")
        # ログインチェック
        user_data = memo_db.get_user_password(user_id)
        if user_data != []:
            if check_password_hash(user_data[0][0], password):
                user = User(user_id)
                login_user(user)
                return redirect("/")
        error_message = "入力されたIDもしくはパスワードが正しくありません"
    return render_template(
        "login.html", user_id=user_id, error_message=error_message
    )


@main.route("/")
@login_required
def index():
    memo_list = memo_db.get_all_memo_data()
    return render_template("index.html", memo_list=memo_list)


@main.route("/user/<name>")
@login_required
def user(name=None):
    return render_template("user.html", name=name)


# メモの登録してメモ一覧に戻る
@main.route("/regist", methods=["GET", "POST"])
@login_required
def regist():
    if request.method == "POST":
        title = request.form.get("title")
        body = request.form.get("body")
        memo_db.insert_new_memo_data(title, body)
        return redirect("/")
    return render_template("regist.html")


# メモの編集してメモ一覧に戻る
@main.route("/<id>/edit", methods=["GET", "POST"])
@login_required
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
@login_required
def delete(id):
    if request.method == "POST":
        memo_db.delete_memo_data(id)
        return redirect("/")
    post = memo_db.get_memo_data(id)
    return render_template("delete.html", post=post[0])
