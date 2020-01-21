# The SmartPod Hardware-Side:

The Hardware-Side of the SmartPod system consists of a Raspberry Pi, an Arduino microcontroller,  a camera, and sensors. The sensors are connected on the Arduino board and the Raspberry Pi sends the collected data received from the Arduino to a Server. 

![The SmartPod Hardware-Side](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1799.jpg)

the Server-Side collects every 5 minutes the following data:

* Room-temperature in Celsius
* Air-humidity in percent
* Soil-humidity in percent
* Image of the plant as JPG

## The Hardware Side consists of the following components:

* [Raspberry Pi](#Raspberry-Pi)
* [Arduino Leonardo](#Arduino-Leonardo)
* [Raspberry Pi Camera Module v1](#Raspberry-Pi-Camera-Module-v1)
* [Iduino Water Sensor (SE045)](#Iduino-Water-Sensor-(SE045))
* [DHT 11 Temperature and Humidity Sensor](#DHT-11-Temperature-and-Humidity-Sensor)

## Raspberry Pi
The Raspberry Pi is a single-board computer and is the main component of the system. The main task of this component is to process and send the collecting data to the server. Furthermore, the Raspberry Pi takes every 5 minutes with the help of an external camera an image. For this project, the [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/) has been used. Important to mention is that the Raspberry Pi needs to be connected permanently to the internet. 

![Raspberry Pi 3 Model B+](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1804.jpg)

### Required Software installed on the Raspberry Pi
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/): Raspbian is the official supported operating system for the Raspberry Pi. It is a Linux Debian-based operating system and for the project, the desktop version of Raspbian Buster (version September 2019) has been used. 

* [Python 3](https://www.python.org/downloads/): On the Raspberry Pi a Python script reads the sensor data, takes the pictures and sends the data to the server. For this, Python 3 needs to be installed on the Raspberry Pi.
For the SmartPod.py script, some external Python packages need to be installed:

     * [PySerial](https://pyserial.readthedocs.io/en/latest/shortintro.html):
     PySerial is a module that encapsulates the access for the serial port in order to receive Sensor data from the 
     Arduino.

     * [Picamera](https://picamera.readthedocs.io/en/release-1.13/): Picamera is a package that provides a Python 
     interface to the Raspberry Pi camera.
     
     * [Flask](https://www.fullstackpython.com/flask.html): A Python web framework

* [Arduino IDE](https://www.arduino.cc/en/Main/Software): The Arduino IDE is a software to develop and upload scripts to the Arduino. Before using the SmpartPod Arduino script the following libraries need to be installed with the Arduino Libary Manager:

     * Adafruit Circuit Playground

     * Adafruit Unified Sensor

     * DHT sensor library

## Arduino Leonardo
The [Arduino Leonardo](https://www.arduino.cc/en/Main/Arduino_BoardLeonardo) is a  microcontroller and is connected via USB to the Raspberry Pi. On the board, a liquid sensor and a humidity/temperature sensor are connected. The main task of the controller is to transfer the data received from the sensors to the Raspberry.

![Arduino Leonardo](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1798.jpg)
 
## Raspberry Pi Camera Module v1
It is a 5MP [camera](https://www.raspberrypi.org/documentation/hardware/camera/) that is connected on the Raspberry Pi.

![Raspberry Pi Camera Module v1](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1805.jpg)

## Iduino Water Sensor (SE045)
It is an [analog water sensor](https://asset.conrad.com/media10/add/160267/c1/-/en/001485323DS01/datenblatt-1485323-iduino-feuchte-sensor-modul-1-st-se045.pdf), that is able to detect water or other fluid that covers the wired area. 

![Iduino Water Sensor (SE045)](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1801.jpg)

## DHT 11 Temperature and Humidity Sensor 
It is a [digital sensor](https://components101.com/dht11-temperature-sensor
) that can measure temperature from 0°C to 50°C and humidity from 20% to 90%.

![DHT 11 Temperature and Humidity Sensor ](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1803.jpg)

## Setup Tutorial:

Before starting the setup make sure that each of the [above-listed components](#Required-Software-installed-on-the-Raspberry-Pi) are installed on the Raspberry Pi otherwise the system will not work properly. 

### Step 1: Connect and set up the camera
After the Raspberry Pi is set up with all the necessary software the camera should be connected on the board. Important to mention is that the camera needs to be enabled in the Raspberry Pi system setting. [This tutorial can be followed to set up the Camera](https://thepihut.com/blogs/raspberry-pi-tutorials/16021420-how-to-install-use-the-raspberry-pi-camera). Then the camera should be fixed in order to focus on the plant that is going to be monitored with the system.

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1809.jpg)

### Step 2: Set up the Arduino

The Arduino needs to be connected to the Raspberry with the help of a USB to Micro USB cable. If the red LED of the Arduino flashes the Arduino is ready to use. 

### Step 4: Connect the Water Sensor:

The red sensor itself needs to be put inside the soil of the plant. Important is that the wires on the sensor needs to be fully covered for accurate data.

![Connect the Water Sensor](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1812.jpg)


The sensor needs to be connected on the Board as followed:

* "+" to 5V
* "-" to GND
* S to A0 (Analog Input 0)

### Step 5: Connect the DHT 11 Temperature and Humidity Sensor:

The Temperature and Humidity Sensor should be placed near the plant. 
The sensor needs to be connected on the Board as followed:

* "+" to 5V
* "-" to GND
* out to Digital (PWM~) 2

note: the Arduino Leonardo is equipped with only one 5V output. So the 5V output needs to be split with the help of a breadboard. 

![breadboard](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1813.jpg)

### Step 6: Upload the "SmartPod.ino" Script to the Arduino
The "SmartPod.ino" script in the "Arduino Scripts" folder needs to be uploaded to the Arduino. To do so the "SmartPod.ino" file needs to be opened with the Arduino IDE. After this, the Arduino Board and Port need to be configured. This has to be done in the "Tools" tab. Now the Script can be uploaded to the Arduino. After the upload, the script runs on the Arduino. To check if the script is able to read the sensor data the build-in Serial Monitor should be executed.

### Step 7: Edit the configuration File
Before executing the "SmartPod.py" script the "SmartPodConfig" file in the Folder "Python Scripts"needs to be edited as followed:

* serialId :  depending on on which USB port the Arduino is connect ('/dev/ttyACM1' or '/dev/ttyACM0')
* plantId : the Id of the plant
* apiCreateMeasurementUrl: the Url of the create.php file for the measurements
* apiCreateImageUrl: the Url of the create.php file for images
* serverImageFolderUrl : The Url of the Image Folder on the Server
* ftpServerUrl : The Url of the ftp-server 
* ftpServerUser : The Username of the ftp-server
* ftpServerPassword : The Password of the ftp-server User

### Step 8: Run the "SmartPod.py" Script
After all the steps above the "SmartPod.py" script in the Folder "Python Scripts" can be executed. 

Now the Script should send the data received from the Arduino to the Server. 






