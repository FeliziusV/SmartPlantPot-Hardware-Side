import serial
import time
import os
import requests
import json
import ftplib
from datetime import datetime
from picamera import PiCamera
from time import sleep
from flask import request

#uploads temperature value to server
def postTemperature(temperature):
    payload = {"plant_id" : 1, "unit" : "celsius", "value" : str(temperature), "type" : "temperature"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)

#uploads air-humidity value to server
def postHumidityAir(humidity):
    payload = {"plant_id" : 1, "unit" : "percent", "value" : str(humidity), "type" : "humidity_air"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)

#uploads soil-humidity value to server
def postHumiditySoil(humidity):
    payload = {"plant_id" : 1, "unit" : "percent", "value" : str(humidity), "type" : "humidity_soil"}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)

#uploads image name to server
def postImageName(name):
    payload = {"plant_id" : 1, "value" : str(name)}
    r = requests.post('http://www.trabby.at/spp/api/measurement/create.php', json=payload)

#returns current time
def getTime():
    dateTimeObj = datetime.now()
    dateTimeObj =dateTimeObj.strftime('%Y-%m-%d %H:%M')
    return dateTimeObj
#takes picture and uploads it to the server
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
    
    session =ftplib.FTP('www12.world4you.com','ftp5166141_felix','felix12345')
    file= open("Images/"+name+".jpg",'rb')
    session.storbinary("STOR images/"+name+".jpg",file)
    file.close()
    session.quit()
    print("image uploaded")
    os.remove("Images/"+name+".jpg")

#-----------------main logic -----------------------
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
                print(timestamp+" - pot humidity: "+str(humidity_pot)+" air humidity: "+str(humidity_air)+" temperature: "+str(temperature))
                postTemperature(str(temperature).rstrip());
                postHumidityAir(str(humidity_air));
                postHumiditySoil(str(humidity_pot));
                takePicture(plantid,timestamp)
                time.sleep(300)
                
            except SerialException:
                print ("Serial Error")
        


