import serial
import time
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from picamera import PiCamera
from time import sleep

  
try:
    connection = mysql.connector.connect(host='mysqlsvr70.world4you.com',
                                             database='5166141db1',
                                             user='sql7063470',
                                             password='9q+4zcu')
    cursor = connection.cursor()
    mySql_insert_query = """SELECT * FROM PLANTS"""

        
        cursor.execute(mySql_insert_query)
        connection.commit()

except mysql.connector.Error as error:
        print("Failed to insert into MySQL table".format(error))
