
import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user, password=db_password,
                                unix_socket=unix_socket, db=db_name,
                                cursorclass=pymysql.cursors.DictCursor
                                )
    except pymysql.MySQLError as e:
        print(e)

    return conn


def get_spaces():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM space;')
        spaces = cursor.fetchall()
        if result > 0:
            got_spaces = jsonify(spaces)
        else:
            got_spaces = 'No space in Database'
    conn.close()
    return got_spaces

def get_spacesallocation():
    conn = open_connection()
    with conn.cursor() as cursor:
        result = cursor.execute('SELECT * FROM spaceallocation;')
        spaces = cursor.fetchall()
        if result > 0:
            got_spaces = jsonify(spaces)
        else:
            got_spaces = 'No spaceallocation in Database'
    conn.close()
    return got_spaces

def add_spaces(spaces):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO space (id, space_name) VALUES(%s, %s)', (spaces["id"], spaces["space_name"]))
    conn.commit()
    conn.close()

def add_spacesallocation(spacesallocation):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO spaceallocation (space_id, timestamp, level, vsize, vname, bay_id) VALUES(%s, %s, %s, %s, %s, %s )', (spacesallocation["space_id"], spacesallocation["timestamp"], spacesallocation["level"], spacesallocation["vsize"], spacesallocation["vname"], spacesallocation["bay_id"]))
    conn.commit()
    conn.close()


