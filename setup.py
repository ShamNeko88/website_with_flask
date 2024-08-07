from models import database_manager

data = database_manager.ConnectSqlite3("data/develop.db")

create_memo_data = """
    CREATE TABLE memo_data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title    TEXT NOT NULL,
        body     TEXT NOT NULL,
        upd_date TEXT NOT NULL
    );
"""
create_user_data = """
    CREATE TABLE user_data(
        user_num  INTEGER PRIMARY KEY AUTOINCREMENT,
        id       TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        upd_date TEXT NOT NULL
    );
"""
data.execute_sql(create_memo_data)
data.execute_sql(create_user_data)
