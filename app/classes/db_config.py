import mysql.connector as MySQLdb
import gc

def connection():
	
	db = MySQLdb.connect(host='localhost', user='root', password='', database='pythonCodeStructure')
	gc.collect()

	return db