import serial
import time
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from picamera import PiCamera
from time import sleep
from flask import request
import requests
import json

def postTemperature(temperature):
    payload = {"plant_id" : 1, "unit" : "celsius", "value" : str(temperature), "type" : "temperature"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)
    print(r.text)
    
def postHumidityAir(humidity):
    payload = {"plant_id" : 1, "unit" : "percent", "value" : str(humidity), "type" : "humidity_air"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)
    print(r.text)
    
def postHumiditySoil(humidity):
    payload = {"plant_id" : 1, "unit" : "percent", "value" : str(humidity), "type" : "humidity_soil"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)
    print(r.text)

def writeToFile(text):
    file = open("data_water.txt","a") 
    file.write(text)
    file.write("\n")
    file.close()
    
def getTime():
    dateTimeObj = datetime.now()
    dateTimeObj =dateTimeObj.strftime('%Y-%m-%d %H:%M')
    return dateTimeObj

def takePicture(plantid,date):
    camera = PiCamera()
    camera.start_preview(fullscreen=False,window=(100,200,300,400))
    sleep(2)
    date=date.replace(' ','')
    date=date.replace('-','')
    date=date.replace(':','')
    name=str(plantid)+date
    camera.capture("Images/"+name+".jpg")
    camera.stop_preview()
    camera.close()

    
    
def insertVariblesIntoTable(date,plant_id, value):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='smartpod',
                                             user='fot',
                                             password='fot')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO humidity (date, plant_id, value) 
                                VALUES (%s, %s, %s) """

        recordTuple = (date, plant_id, value)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            
            
ser = serial.Serial('/dev/ttyACM0', 9600)
plantid=1;

while 1: 
    if ser.readline()!=None:
            try:
                line = ser.readline()
                line =line.decode('utf-8')
                timestamp=getTime()
                values=line.split(" ")
               
                humidity_pot=int(values[0])/1023*100
                humidity_pot=round(humidity_pot,2)
                
                humidity_air=float(values[1])
                temperature=values[2];
                print(timestamp+"- pot humidity: "+str(humidity_pot)+" air humidity: "+str(humidity_air)+" temperature: "+str(temperature))
                postTemperature(str(temperature).rstrip());
                postHumidityAir(str(humidity_air));
                postHumiditySoil(str(humidity_pot));
                #writeToFile(str(getTime())+" - "+line.decode('utf-8'))
            
                #insertVariblesIntoTable(timestamp,1,humidity_pot)
                takePicture(plantid,timestamp)
                time.sleep(300)
            except SerialException:
                print ("error ")
        


