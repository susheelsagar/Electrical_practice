__author__ = 's'
import mysql.connector

def connect():
 cnx = mysql.connector.connect(user='root', password='',
                              host='127.0.0.1',
                             database='dss')
 c = cnx.cursor();
 c.execute("show tables")
 for(a) in c :
     print a
 c.close();
 cnx.close




