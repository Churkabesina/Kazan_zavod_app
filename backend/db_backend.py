import os
import sys
from PySide6 import QtSql

class Database:
    def __init__(self, db_driver: str, db_path: str):
        """
        db_driver - QSQLITE, ,mysql, pgsql...
        db - открытие закрытие подключения через него
        """
        self.db_driver = db_driver
        self.db_path = db_path + r'/database.db'
        self.db = QtSql.QSqlDatabase.addDatabase(self.db_driver)
        self.db.setDatabaseName(self.db_path)

    def create_db(self):
        """Проверка существования и создание базы данных"""
        if not os.path.exists(self.db_path):
            if not self.db.open():
                print(f"Ошибка при создании базы данных: {self.db.lastError().text()}")
                sys.exit(1)

            query = QtSql.QSqlQuery()
            ##### склад
            sql_table_storage = ''' 
                                CREATE TABLE IF NOT EXISTS storage (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                type_metal TEXT NOT NULL,
                                size TEXT,
                                balance_kg REAL,
                                balance_mm REAL,
                                UNIQUE(type_metal, size)
                                );
                                '''
            ##### база продукции
            sql_table_products = '''
                                CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                product TEXT,
                                type_metal TEXT,
                                mark_steel TEXT,
                                diameter TEXT,
                                lenght REAL,
                                draw TEXT,
                                FOREIGN KEY (type_metal) REFERENCES storage(type_metal),
                                FOREIGN KEY (diameter) REFERENCES storage(size)
                                );
                                '''
            ##### временная продукция на выгрузку в счета
            sql_table_temp_products = '''
                                        CREATE TABLE IF NOT EXISTS temp_products (
                                        id INTEGER PRIMARY KEY,
                                        product TEXT DEFAULT NULL,
                                        count INTEGER DEFAULT NULL,
                                        type_metal TEXT DEFAULT NULL,
                                        mark_steel TEXT DEFAULT NULL,
                                        diameter TEXT DEFAULT NULL,
                                        lenght REAL DEFAULT NULL,
                                        weight REAL DEFAULT NULL,
                                        draw TEXT DEFAULT NULL
                                        );
                                        '''
            ##### счета
            sql_table_deals = '''CREATE TABLE IF NOT EXISTS products_four (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''
            ##### главный экран
            sql_table_leads = '''CREATE TABLE IF NOT EXISTS products_four (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, price REAL)'''

            # sqllite не умеет в много запросность
            self._exec_sql_statement(query, sql_table_temp_products)
            self._exec_sql_statement(query, sql_table_products)
            self._exec_sql_statement(query, sql_table_storage)
            self._exec_sql_statement(query, sql_table_deals)
            self._exec_sql_statement(query, sql_table_leads)
            self.db.close()

    @staticmethod
    def _exec_sql_statement(query: QtSql.QSqlQuery, sql_statement: str = None):
        if sql_statement:
            if not query.exec(sql_statement):
                print(f"Ошибка при выполнении неподготовленного запроса: {query.lastError().text()}")
                sys.exit(1)
        else:
            if not query.exec():
                print(f"Ошибка при выполнении подготовленного (.prepare) запроса: {query.lastError().text()}")
                sys.exit(1)

    # открытие соединения, использовать только внутри этого класса
    def _open_db(self):
        if not self.db.open():
            print(f"Ошибка при подключении к базе данных: {self.db.lastError().text()}")
            sys.exit(1)

    ### методы к временной таблице - TEMP TABLE
    def add_temp_table_row(self, next_id: int):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''INSERT INTO temp_products (id) VALUES (?)'''
        query.prepare(statement)
        query.bindValue(0, next_id)
        self._exec_sql_statement(query)
        self.db.close()

    def select_last_id_temp_table(self) -> int | None:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT MAX(id) FROM temp_products'''
        self._exec_sql_statement(query, statement)
        query.next()
        print(f'backend func select_next_id_temp_table: query.value = {query.value(0)}')
        self.db.close()
        if query.value(0) == '':
            return None
        return int(query.value(0))

    def del_temp_table_row(self, row_id: int):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''DELETE FROM temp_products WHERE id = ?'''
        query.prepare(statement)
        print(f'backend func del_temp_table_row: row_id = {row_id}')
        query.bindValue(0, row_id)
        self._exec_sql_statement(query)
        self.db.close()

    def select_temp_table_rows(self) -> list[list]:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM temp_products'''
        self._exec_sql_statement(query, statement)
        selected_data = []
        while query.next():
            selected_data.append([query.value(x) for x in range(query.record().count())])
        # print(f'backend func select_temp_table_rows: selected_data = {selected_data}')
        self.db.close()
        return selected_data

    def del_temp_table_all_rows(self):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''DELETE FROM temp_products'''
        self._exec_sql_statement(query, statement)
        self.db.close()
    ### методы к временной таблице - TEMP TABLE

    ### методы к таблице продукции - PRODUCTS TABLE
    def select_products(self) -> list:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT product from products'''
        self._exec_sql_statement(query, statement)
        selected_data = []
        while query.next():
            selected_data.append(query.value(0))
        self.db.close()
        return selected_data
    ### методы к таблице продукции - PRODUCTS TABLE

    ### методы к таблице склада - STORAGE TABLE
    def select_storage_table_rows(self) -> list[list]:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM storage'''
        self._exec_sql_statement(query, statement)
        selected_data = []
        while query.next():
            selected_data.append([query.value(x) for x in range(query.record().count())])
        print(selected_data)
        return selected_data

    def select_type_metal_and_size(self) -> dict[str, dict]:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT id, type_metal, size FROM storage'''
        self._exec_sql_statement(query, statement)
        selected_data = {}
        while query.next():
            if query.value(1) not in selected_data:
                selected_data[query.value(1)] = {query.value(2): query.value(0)}
            else:
                selected_data[query.value(1)][query.value(2)] = query.value(0)
        self.db.close()
        return selected_data

    def update_balance_kg_and_mm(self, type_metal: str, size: str | None, new_kg: float, new_mm: float | None):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''UPDATE storage SET balance_kg = :kg, balance_mm = :mm WHERE type_metal = :metal and size = :size'''
        query.prepare(statement)
        query.bindValue(':kg', new_kg)
        query.bindValue(':mm', new_mm)
        query.bindValue(':metal', type_metal)
        query.bindValue(':size', size)
        self._exec_sql_statement(query)
        self.db.close()