import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

connection = sqlite3.connect(ROOT_PATH / "my_database.db")
cursor = connection.cursor()
cursor.row_factory = sqlite3.Row

cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='clients';")
table_exists = cursor.fetchone()

def create_table_clients(connection, cursor):
    cursor.execute("CREATE TABLE clients (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))")
    connection.commit()

def insert_register(connection, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clients (nome, email) VALUES (?,?);", data)
    connection.commit()

def update_register(connection, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clients SET nome=?, email=? WHERE id=?;", data)
    connection.commit()

def delete_register(connection, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clients WHERE id=?", data)
    connection.commit()

def insert_many(connection, cursor, data):
    # data = [("charles", "charles@email.com"), ("admin", "admin@email.com")]
    cursor.executemany("INSERT INTO clients (nome, email) VALUES (?,?);", data)
    connection.commit()

def select_all(cursor):
    cursor.execute("SELECT * FROM clients;")
    registers = cursor.fetchall()
    print(registers)
    for client in registers:
        print(dict(client))

def select_one(cursor, id):
    cursor.execute("SELECT * FROM clients WHERE id=?;", (id,))
    register = cursor.fetchone()
    print(dict(register))

if table_exists:
    # select_one(cursor, 2)
    select_all(cursor)
else:
    create_table_clients(connection, cursor)
    insert_register(connection, cursor, "Admin", "admin@email.com")

connection.close()