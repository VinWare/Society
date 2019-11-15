import pymysql

HOST     = 'localhost'
USER     = 'root'
PASSWD   = 'c1o0l0d8'
DATABASE = 'society_mysqldb'
def connection():
	conn = pymysql.connect(host = HOST, user = USER, passwd = PASSWD, db = DATABASE)
	cursor = conn.cursor()
	return conn, cursor
