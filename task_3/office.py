import sqlite3


def create_tables(cursor: sqlite3.Cursor):
    """
    Создает таблицы в базе данных, если они не существуют.

    :param cursor: Объект курсора базы данных.
    """
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Cities (
            city_id INTEGER PRIMARY KEY,
            city_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Companies (
            company_id INTEGER PRIMARY KEY,
            company_name TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Offices (
            office_id INTEGER PRIMARY KEY,
            office_name TEXT,
            company_id INTEGER,
            city_id INTEGER,
            FOREIGN KEY (company_id) REFERENCES Companies(company_id),
            FOREIGN KEY (city_id) REFERENCES Cities(city_id)
        )
    ''')


def insert_data(cursor: sqlite3.Cursor, table: str, data: list):
    """
    Вставляет данные в таблицу.

    :param cursor: Объект курсора базы данных.
    :param table: Имя таблицы ('Cities', 'Companies' или 'Offices').
    :param data: Данные для вставки в формате списка кортежей.
    """
    if table == 'Cities':
        query = 'INSERT INTO Cities (city_name) VALUES (?)'
    elif table == 'Companies':
        query = 'INSERT INTO Companies (company_name) VALUES (?)'
    elif table == 'Offices':
        query = 'INSERT INTO Offices (office_name, company_id, city_id) VALUES (?, ?, ?)'

    cursor.executemany(query, data)


def company_offices(cursor: sqlite3.Cursor, company_id: int):
    """
    Возвращает список офисов определенной компании.

    :param cursor: Объект курсора базы данных.
    :param company_id: ID компании.
    :return: Список офисов компании.
    """
    cursor.execute('SELECT office_name FROM Offices WHERE company_id = ?', (company_id,))
    return cursor.fetchall()


def company_offices_in_city(cursor: sqlite3.Cursor, company_id: int, city_id: int):
    """
    Возвращает список офисов определенной компании в определенном городе.

    :param cursor: Объект курсора базы данных.
    :param company_id: ID компании.
    :param city_id: ID города.
    :return: Список офисов компании в указанном городе.
    """
    cursor.execute('SELECT office_name FROM Offices WHERE company_id = ? AND city_id = ?', (company_id, city_id))
    return cursor.fetchall()


def companies_in_city(cursor: sqlite3.Cursor, city_id: int):
    """
    Возвращает список уникальных компаний, имеющих офисы в определенном городе.

    :param cursor: Объект курсора базы данных.
    :param city_id: ID города.
    :return: Список уникальных компаний в указанном городе.
    """
    cursor.execute(
        'SELECT DISTINCT C.company_name '
        'FROM Companies C '
        'JOIN Offices O ON C.company_id = O.company_id '
        'WHERE O.city_id = ?',
        (city_id,))
    return cursor.fetchall()


if __name__ == '__main__':
    with sqlite3.connect('office_database.db') as conn:
        cursor = conn.cursor()

        create_tables(cursor)

        cities_data = [
            ('New York',),
            ('San Francisco',),
            ('Moscow',)
        ]

        companies_data = [
            ('Company A',),
            ('Company B',),
            ('Company C',),
        ]

        offices_data = [
            ('Office 1', 1, 1),
            ('Office 2', 1, 2),
            ('Office 3', 2, 1),
            ('Office 4', 2, 3),
            ('Office 5', 3, 2),
            ('Office 6', 3, 3),
        ]
        insert_data(cursor, 'Cities', cities_data)
        insert_data(cursor, 'Companies', companies_data)
        insert_data(cursor, 'Offices', offices_data)

        print('Офисы Company A:', company_offices(cursor, 1))
        print('Офисы Company B в городе New York:', company_offices_in_city(cursor, 2, 1))
        print('Фирмы в городе Moscow:', companies_in_city(cursor, 3))
