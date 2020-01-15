import serial
import time
import os
import requests
import json
import ftplib
import SmartPodConfig as cfg
from datetime import datetime
from picamera import PiCamera
from time import sleep
from flask import request

#uploads temperature value to server
def postTemperature(temperature):
    payload = {"plant_id" : cfg.general['plantId'], "unit" : "celsius", "value" : str(temperature), "type" : "temperature"}
    r = requests.post(cfg.general['serverUrlMeasurement'], json=payload)

#uploads air-humidity value to server
def postHumidityAir(humidity):
    payload = {"plant_id" : cfg.general['plantId'], "unit" : "percent", "value" : str(humidity), "type" : "humidity_air"}
    r = requests.post(cfg.general['serverUrlMeasurement'], json=payload)

#uploads soil-humidity value to server
def postHumiditySoil(humidity):
    payload = {"plant_id" : cfg.general['plantId'], "unit" : "percent", "value" : str(humidity), "type" : "humidity_soil"}
    r = requests.post(cfg.general['serverUrlMeasurement'], json=payload)

#uploads image name to server
def postImageName(name):
    payload = {"plant_id" : cfg.general['plantId'], "path" : cfg.general['serverUrlImageFolder']+str(name)}
    r = requests.post(cfg.general['serverUrlImage'], json=payload)
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
    
    session =ftplib.FTP(cfg.general['ftpUrl'],cfg.general['ftpUser'],cfg.general['ftpPassword'])
    file= open("Images/"+name+".jpg",'rb')
    session.storbinary("STOR images/"+name+".jpg",file)
    file.close()
    session.quit()
    print("image uploaded")
    os.remove("Images/"+name+".jpg")
    postImageName(name+".jpg")
    

#-----------------main logic -----------------------
ser = serial.Serial(cfg.general['serialId'], 9600)
plantid=cfg.general['plantId'];

while 1: 
    if ser.readline()!=None:
            try:
                line = ser.readline()
                line =line.decode('utf-8')
                timestamp=getTime()
                values=line.split(" ")
                humidity_pot=float(values[0])/1023*100
                humidity_pot=round(humidity_pot,2)
                humidity_air=float(values[1])
                temperature=values[2];
                print(timestamp+" - pot humidity: "+str(humidity_pot)+" air humidity: "+str(humidity_air)+" temperature: "+str(temperature))
                postTemperature(str(temperature).rstrip());
                postHumidityAir(str(humidity_air));
                postHumiditySoil(str(humidity_pot));
                takePicture(plantid,timestamp)
                
                time.sleep(300)
            except requests.exceptions.Timeout:
                print("Connection error")
                continue
            except serial.SerialException:
                print ("Serial Error")
                continue
        


