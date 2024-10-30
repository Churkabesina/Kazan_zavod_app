import os
import sys
from os.path import exists

from PySide6 import QtSql

class Database:
    def __init__(self, db_driver: str, db_folder: str):
        """
        db_driver - QSQLITE, ,mysql, pgsql...
        db - открытие закрытие подключения через него
        """
        self.db_driver = db_driver
        self.db_folder = db_folder
        self.db_path = self.db_folder + r'/database.db'
        self.db = QtSql.QSqlDatabase.addDatabase(self.db_driver)
        self.db.setDatabaseName(self.db_path)

    def create_db(self):
        """Проверка существования и создание базы данных"""
        if not os.path.exists(self.db_folder):
            os.mkdir(self.db_folder)
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
                                weight REAL,
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
                                        total_weight REAL DEFAULT NULL,
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
            self._exec_sql_statement(query, sql_table_storage)
            self._exec_sql_statement(query, sql_table_products)
            self._exec_sql_statement(query, sql_table_temp_products)
            self._exec_sql_statement(query, sql_table_deals)
            self._exec_sql_statement(query, sql_table_leads)

            # add_base_metal_1 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 2" 2АУ.21.003', NULL, 0, NULL)'''
            # add_base_metal_2 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 2.5" 2АУ.21.003-10', NULL, 0, NULL)'''
            # add_base_metal_3 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 3" 2АУ.21.003-20', NULL, 0, NULL)'''
            # add_base_metal_4 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 4" 70 Мпа 2АУ21003-40', NULL, 0, NULL)'''
            # add_base_metal_5 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 4" 2уха 4.320', NULL, 0, NULL)'''
            # add_base_metal_6 = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES ('Гайка 4" 3уха 4.14.002', NULL, 0, NULL)'''

            # self._exec_sql_statement(query, add_base_metal_1)
            # self._exec_sql_statement(query, add_base_metal_2)
            # self._exec_sql_statement(query, add_base_metal_3)
            # self._exec_sql_statement(query, add_base_metal_4)
            # self._exec_sql_statement(query, add_base_metal_5)
            # self._exec_sql_statement(query, add_base_metal_6)

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
        self.db.close()
        return selected_data

    def del_temp_table_all_rows(self):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''DELETE FROM temp_products'''
        self._exec_sql_statement(query, statement)
        self.db.close()

    def update_temp_table_row_by_id(self, _id: int, update_data: dict):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''UPDATE temp_products SET product = ?, count = ?, type_metal = ?, mark_steel = ?, diameter = ?, lenght = ?, total_weight = ?, draw = ? WHERE id = ?'''
        query.prepare(statement)
        query.bindValue(0, update_data['product'])
        query.bindValue(1, 1)
        query.bindValue(2, update_data['type_metal'])
        query.bindValue(3, update_data['mark_steel'])
        query.bindValue(4, update_data['diameter'])
        query.bindValue(5, update_data['lenght'])
        query.bindValue(6, update_data['weight'])
        query.bindValue(7, update_data['draw'])
        query.bindValue(8, _id)
        self._exec_sql_statement(query)
        self.db.close()

    def update_temp_table_count_and_total_weight_by_id(self, _id: int, count: int, total_weight: float | None):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''UPDATE temp_products SET count = ?, total_weight = ? WHERE id = ?'''
        query.prepare(statement)
        query.bindValue(0, count)
        query.bindValue(1, total_weight)
        query.bindValue(2, _id)
        self._exec_sql_statement(query)
        self.db.close()

    ### методы к временной таблице - TEMP TABLE

    ### методы к таблице продукции - PRODUCTS TABLE
    def select_products_db_rows(self) -> list[list]:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM products'''
        self._exec_sql_statement(query, statement)
        selected_data = []
        while query.next():
            selected_data.append([query.value(x) for x in range(query.record().count())])
        self.db.close()
        return selected_data

    def select_all_products_products_db(self) -> list:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT product from products'''
        self._exec_sql_statement(query, statement)
        selected_data = []
        while query.next():
            selected_data.append(query.value(0))
        self.db.close()
        return selected_data

    def select_products_db_row_by_product(self, product: str) -> dict:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM products WHERE  product = ?'''
        query.prepare(statement)
        query.bindValue(0, product)
        self._exec_sql_statement(query)
        query.next()
        selected_data = {query.record().fieldName(x): query.value(x) for x in range(query.record().count())}
        self.db.close()
        return selected_data

    def check_product_exists_products_db(self, product: str) -> bool:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT 1 FROM products WHERE  product = ?'''
        query.prepare(statement)
        query.bindValue(0, product)
        self._exec_sql_statement(query)
        query.next()
        _exists = query.value(0)
        self.db.close()
        return bool(_exists)

    def insert_product_products_db(self,
                                   product: str,
                                   type_metal: str,
                                   mark_steel: str | None,
                                   diameter: str,
                                   lenght: float,
                                   weight: float | None,
                                   draw: str | None):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''INSERT INTO products (product, type_metal, mark_steel, diameter, lenght, weight, draw) VALUES (?, ?, ?, ?, ?, ?, ?)'''
        query.prepare(statement)
        query.bindValue(0, product)
        query.bindValue(1, type_metal)
        query.bindValue(2, mark_steel)
        query.bindValue(3, diameter)
        query.bindValue(4, lenght)
        query.bindValue(5, weight)
        query.bindValue(6, draw)
        self._exec_sql_statement(query)
        self.db.close()

    def select_last_row_products_db(self) -> list:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM products ORDER BY id DESC LIMIT 1'''
        self._exec_sql_statement(query, statement)
        query.next()
        selected_data = [query.value(x) for x in range(query.record().count())]
        self.db.close()
        return selected_data

    def select_product_weight_by_product_product_db(self, product: str) -> float:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT weight FROM products WHERE  product = ?'''
        query.prepare(statement)
        query.bindValue(0, product)
        self._exec_sql_statement(query)
        query.next()
        weight = query.value(0)
        self.db.close()
        return weight

    def del_product_products_db_by_id(self, _id: int):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''DELETE FROM products WHERE id = ?'''
        query.prepare(statement)
        query.bindValue(0, _id)
        self._exec_sql_statement(query)
        self.db.close()
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
        self.db.close()
        return selected_data

    def select_storage_table_type_metal_and_size(self) -> dict[str, dict]:
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

    def update_storage_table_balance_kg_and_mm(self, type_metal: str, size: str | None, new_kg: float, new_mm: float | None):
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

    def insert_row_storage_table(self, type_metal: str, size: str):
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''INSERT INTO storage (type_metal, size, balance_kg, balance_mm) VALUES (:type_metal, :size, 0, 0)'''
        query.prepare(statement)
        query.bindValue(':type_metal', type_metal)
        query.bindValue(':size', size)
        self._exec_sql_statement(query)
        self.db.close()

    def check_metal_exists_storage_table(self, type_metal: str, size: str) -> bool:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT EXISTS(SELECT 1 FROM storage WHERE type_metal = :type_metal AND size = :size)'''
        query.prepare(statement)
        query.bindValue(':type_metal', type_metal)
        query.bindValue(':size', size)
        self._exec_sql_statement(query)
        query.next()
        _exists = query.value(0)
        self.db.close()
        return bool(_exists)

    def select_last_row_storage_table(self) -> list:
        self._open_db()
        query = QtSql.QSqlQuery()
        statement = '''SELECT * FROM storage ORDER BY id DESC LIMIT 1'''
        self._exec_sql_statement(query, statement)
        query.next()
        selected_data = [query.value(x) for x in range(query.record().count())]
        self.db.close()
        return selected_data