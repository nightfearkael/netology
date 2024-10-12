import psycopg2


class PgConnector:
    def __init__(self, db_host, db_port, db_database, db_user, db_password):
        self.db_host = db_host
        self.db_port = db_port
        self.database = db_database
        self.user = db_user
        self.password = db_password
        self.table = 'clients'
        self.connection = psycopg2.connect(host=self.db_host,
                                           database=self.database,
                                           port=self.db_port,
                                           user=self.user,
                                           password=self.password)
        self.cursor = self.connection.cursor()

    def create_table(self):
        """
        Функция, создающая структуру БД
        """
        sql = '''CREATE TABLE IF NOT EXISTS clients(
                    id SERIAL PRIMARY KEY,
                    first_name VARCHAR(40),
                    last_name VARCHAR(40),
                    email VARCHAR(60) UNIQUE,
                    phones text[]
                    )'''
        self.cursor.execute(sql)
        self.connection.commit()

    def create_client(self, first_name: str, last_name: str, email: str, phones: list = None):
        """
        Функция, позволяющая добавить нового клиента.
        :param first_name: Имя клиента (строка)
        :param last_name: Фамилия клиента (строка)
        :param email: Email клиента (строка)
        :param phones: Телефоны клиента (список)
        """
        sql = f'INSERT INTO {self.table} (first_name, last_name, email, phones) VALUES ((%s), (%s), (%s), (%s))'
        self.cursor.execute(sql, (first_name, last_name, email, phones, ))
        self.connection.commit()

    def add_phone_to_client(self, phone: str, client_id: int):
        """
        Функция, позволяющая добавить телефон для существующего клиента.
        :param phone: Телефон клиента (строка)
        :param client_id: ID клиента
        """
        sql = f"UPDATE {self.table} SET phones = array_append(phones, (%s)) where id=(%s)"
        self.cursor.execute(sql, (phone, client_id, ))
        self.connection.commit()

    def update_client(self, client_id: int, first_name: str = None, last_name: str = None, email: str = None, phones: list = None):
        """
        Функция, позволяющая изменить данные о клиенте.
        :param client_id: ID клиента
        :param first_name: Имя клиента (строка)
        :param last_name: Фамилия клиента (строка)
        :param email: Email клиента (строка)
        :param phones: Телефоны клиента (список)
        :return: None
        """
        sql = (f"""UPDATE {self.table} SET 
                    first_name = CASE WHEN (%s) IS NOT NULL THEN (%s) ELSE first_name END,
                    last_name = CASE WHEN (%s) IS NOT NULL THEN (%s) ELSE last_name END,
                    email = CASE WHEN (%s) IS NOT NULL THEN (%s) ELSE email END,
                    phones = CASE WHEN (%s) IS NOT NULL THEN (%s) ELSE phones END
                    WHERE id=(%s)""")
        self.cursor.execute(sql, (first_name, first_name, last_name, last_name, email, email, phones, phones, client_id, ))
        self.connection.commit()

    def del_phone_from_client(self, phone: str, client_id: int):
        """
        Функция, позволяющая удалить телефон для существующего клиента.
        :param phone: Телефоны клиента (список)
        :param client_id: ID клиента
        """
        sql = f"UPDATE {self.table} SET phones = array_remove(phones, (%s)) where id=(%s)"
        self.cursor.execute(sql, (phone, client_id, ))
        self.connection.commit()

    def delete_client(self, client_id: int):
        """
        Функция, позволяющая удалить существующего клиента.
        :param client_id: ID клиента
        """
        sql = f'DELETE FROM {self.table} WHERE id=(%s)'
        self.cursor.execute(sql, (client_id, ))
        self.connection.commit()

    def find_client(self, first_name: str = None, last_name: str = None, email: str = None, phones: list = None):
        """
        Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
        :param first_name: Имя клиента (строка)
        :param last_name: Фамилия клиента (строка)
        :param email: Email клиента (строка)
        :param phones: Телефоны клиента (список)
        :return: Список кортежей
        """
        sql = f"""SELECT * FROM {self.table}
                    WHERE (first_name = (%s) OR (%s) IS NULL)
                    AND (last_name = (%s) OR (%s) IS NULL)
                    AND (email = (%s) OR (%s) IS NULL)
                    AND (phones = (%s) OR (%s) IS NULL)
                """
        self.cursor.execute(sql, (first_name, first_name, last_name, last_name, email, email, phones, phones))
        result = self.cursor.fetchall()
        return result

    def __del__(self):
        """
        Нужно для завершения сессии подключения к СУБД
        :return: None
        """
        self.connection.close()

