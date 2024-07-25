from models import database_manager

DATABASE = "data/develop.db"

memo_list: list = [
    {"title": "test01", "body": "mkです。"},
    {"title": "test01", "body": "mk２です。"}
]


def get_all_memo_data() -> list:
    db = database_manager.ConnectSqlite3(DATABASE)
    sql = "SELECT * FROM memo_data"
    result: list = db.execute_sql(sql, get_result=True)
    print(result)
    return result
