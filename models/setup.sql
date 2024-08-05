-- メモデータ
CREATE TABLE memo_data(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT NOT NULL,
    body     TEXT NOT NULL,
    upd_date TEXT NOT NULL
);

-- ユーザー情報
CREATE TABLE user_data(
    user_num  INTEGER PRIMARY KEY AUTOINCREMENT,
    id       TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    upd_date TEXT NOT NULL
);