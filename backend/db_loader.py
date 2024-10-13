import os
import sys
from PySide6 import QtSql


def load_db(db_path: str):
    db_path = db_path + r'/database.db'
    # Проверка существования и создание базы данных
    if not os.path.exists(db_path):
        conn = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        conn.setDatabaseName(db_path)
        if not conn.open():
            print(f"Ошибка при создании базы данных: {conn.lastError().text()}")
            sys.exit(1)

        query = QtSql.QSqlQuery()
        sql_table_1 = '''CREATE TABLE IF NOT EXISTS products_one (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''
        sql_table_2 = '''CREATE TABLE IF NOT EXISTS products_two (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''
        sql_table_3 = '''CREATE TABLE IF NOT EXISTS products_three (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''
        sql_table_4 = '''CREATE TABLE IF NOT EXISTS products_four (
        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''
        # sqllite не умеет в много запросность
        sql_executor(query, sql_table_1)
        sql_executor(query, sql_table_2)
        sql_executor(query, sql_table_3)
        sql_executor(query, sql_table_4)

        conn.close()

    # Подключение к базе данных
    db = QtSql.QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(db_path)
    if not db.open():
        print(f"Ошибка подключения к базе данных: {db.lastError().text()}")
        sys.exit(1)

    return db

def sql_executor(query: QtSql.QSqlQuery, sql_statement: str):
    if not query.exec(sql_statement):
        print(f"Ошибка при создании таблицы: {query.lastError().text()}")
        sys.exit(1)