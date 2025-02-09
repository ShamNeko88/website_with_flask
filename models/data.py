from models import database_manager

DATABASE = "data/develop.db"


class MemoManager():
    """
    メモデータ用データベース操作クラス

    Methods:
        insert_new_memo_data: 新しいメモを追加
        get_all_memo_data: 全てのメモデータを取得
        get_memo_data: メモデータをID指定で受け取る
        edit_memo_data: メモデータをID指定で編集する
    """
    def __init__(self):
        self.db = database_manager.ConnectSqlite3(DATABASE)

    # 新しいメモを追加
    def get_all_memo_data(self) -> list:
        sql = "SELECT * FROM memo_data"
        result: list = self.db.execute_sql(sql, get_result=True)
        return result

    def insert_new_memo_data(self, title, body):
        sql = f"""
            INSERT INTO memo_data(
                title,
                body,
                upd_date
            )
            VALUES(
                '{title}',
                '{body}',
                DATETIME('now', 'localtime')
            );
        """
        self.db.execute_sql(sql)

    # id指定でメモのデータを受け取る
    def get_memo_data(self, id: int):
        sql = f"""
            SELECT
                id,
                title,
                body
            FROM
                memo_data
            WHERE
                id = '{id}'
        """
        result = self.db.execute_sql(sql, get_result=True)
        return result

    # id指定でメモの内容を編集する
    def edit_memo_data(self, id: int, title: str, body: str):
        sql = f"""
            UPDATE
                memo_data
            SET
                title = '{title}',
                body = '{body}',
                upd_date = DATETIME('now', 'localtime')
            WHERE
                id = {id}
        """
        self.db.execute_sql(sql)

    # id指定でメモの内容を削除する
    def delete_memo_data(self, id: int):
        sql = f"""
            DELETE FROM
                memo_data
            WHERE
                id = {id}
        """
        self.db.execute_sql(sql)

    # ユーザーの新規作成
    def insert_new_user(self, id, hashed_password):
        sql = f"""
            INSERT INTO user_data(
                id,
                password,
                upd_date
            )
            VALUES(
                '{id}',
                '{hashed_password}',
                DATETIME('now', 'localtime')
            )
        """
        self.db.execute_sql(sql)

    # id指定して抽出
    def get_user(self, id):
        sql = (
            f"SELECT          "
            f"    id          "
            f"FROM            "
            f"    user_data   "
            f"WHERE           "
            f"    id = '{id}' "
        )
        result = self.db.execute_sql(sql, get_result=True)
        return result

    # ログイン時のパスワード検証
    def get_user_password(self, id):
        sql = (
            f"SELECT          "
            f"    password    "
            f"FROM            "
            f"    user_data   "
            f"WHERE           "
            f"    id = '{id}' "
        )
        result = self.db.execute_sql(sql, get_result=True)
        return result


def insert_test_data():
    db = database_manager.ConnectSqlite3(DATABASE)
    delete_data = "DELETE FROM memo_data WHERE title = 'テストデータ';"
    insert_data = """
        INSERT INTO memo_data(
            title,
            body,
            upd_date
        )
        VALUES(
            'テストデータ',
            'テストボディ２',
            DATETIME('now', 'localtime')
        );
    """
    db.execute_sql(delete_data)
    db.execute_sql(insert_data)
