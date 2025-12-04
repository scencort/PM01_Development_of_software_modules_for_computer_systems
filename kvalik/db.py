import pymysql
from pymysql import cursors

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="2281337",
        database="hotel_cval",
        cursorclass=pymysql.cursors.DictCursor
    )