import mysql.connector as MySQLdb
import time
import datetime
import socket

# import MySQLdb.cursors
import re





db = MySQLdb.connect(host='localhost', user='root', password='')

cursor = db.cursor()



#DROP DATABASE IF IT ALREADY EXIST AND CREATE A NEW DATABASE

cursor.execute('DROP DATABASE IF EXISTS pythonCodeStructure')
cursor.execute('CREATE DATABASE pythonCodeStructure DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci')
cursor.execute('USE pythonCodeStructure')



#CREATE TABLE TO HOLD USER LOGIN INFORMATION
cursor.execute('CREATE TABLE Users_Login(username VARCHAR(11) PRIMARY KEY, password VARCHAR(400), login_ip VARCHAR(40), last_login TIMESTAMP NULL, created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, updated_at TIMESTAMP NULL) ENGINE = InnoDB')

#CREATE TABLE TO HOLD USER BASIC INFORMATION





#CREATE TABLE TO HOLD USER COMPLETE CONTACT AND ADDRESS INFORMATION


#CREATE TABLE TO HOLD USER FORGOT PASSWORD REQUESTS

