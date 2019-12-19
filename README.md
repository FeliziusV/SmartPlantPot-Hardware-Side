# The SmartPod Hardware-Side:

The Hardware Side of the SmartPod system consists of a Raspberry Pi, an Arduino microcontroller,  a camera, and sensors. The sensors are connected on the Arduino board and the Raspberry Pi sends the collected data received from the Arduino to a Server. 

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1799.jpg)

## The Hardware Side consists of the following components:

* Raspberry Pi
* Arduino Leonardo
* Raspberry Pi Camera Module v1
* Iduino Water Sensor (SE045)
* DHT 11 Temperature and Humidity Sensor

## Raspberry Pi
The Raspberry Pi is a single-board computer and is the main component of the system. The main task of this component is to process and send the collecting data to the server. Furthermore, the Raspberry Pi takes every 5 minutes with the help of an external camera an image. For this project, the [Raspberry Pi 3 Model B+](https://www.raspberrypi.org/products/raspberry-pi-3-model-b-plus/)  has been used. Important to mention is that the Raspberry Pi needs to be connected permanently to the internet. 

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1804.jpg)

### Required Software installed on the Raspberry Pi
* [Raspbian](https://www.raspberrypi.org/downloads/raspbian/): Raspbian is the official supported operating system for the Raspberry Pi. It is a Linux Debian-based operating system and for the project, the desktop version of Raspbian Buster (version September 2019) has been used. 


* [Python 3](https://www.python.org/downloads/): On the Raspberry Pi a python script reads the sensor data, takes the pictures and sends the data to the server. For this, Python 3 needs to be installed on the Raspberry Pi.
For the SmartPod.py script, some Python Packages need to be installed:

     * [PySerial](https://pyserial.readthedocs.io/en/latest/shortintro.html):
     PySerial is a module that encapsulates the access for the serial port in order to receive Sensor data from the 
     Arduino.

     * [Picamera](https://picamera.readthedocs.io/en/release-1.13/): Picamera is a package that provides a pure Python 
     interface to the Raspberry Pi camera.

* [Arduino IDE](https://www.arduino.cc/en/Main/Software): The Arduino IDE is software to develop and upload Scripts to the Arduino. Before using the SmpartPod Arduino Script the following libraries need to be installed with the Arduino Libary Manager:

     * Adafruit Circuit Playground

     * Adafruit Unified Sensor

     * DHT sensor library
## Arduino Leonardo:
The [Arduino Leonardo](https://www.arduino.cc/en/Main/Arduino_BoardLeonardo) is a  microcontroller and is connected via USB to the Raspberry Pi. On the board, a liquid sensor and a humidity/temperature sensor are connected. The main task of the controller is to transfer the data received from the sensors to the Raspberry.

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1798.jpg)
 
## Raspberry Pi Camera Module v1:
Is a 5MP [camera](https://www.raspberrypi.org/documentation/hardware/camera/) that is connected on the Raspberry Pi.

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1805.jpg)

## Iduino Water Sensor (SE045):
It is an [analog water sensor](https://asset.conrad.com/media10/add/160267/c1/-/en/001485323DS01/datenblatt-1485323-iduino-feuchte-sensor-modul-1-st-se045.pdf), that is able to detect water or other fluid covers the wire area or not. 

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1801.jpg)

## DHT 11 Temperature and Humidity Sensor: 
Is a [digital sensor](https://components101.com/dht11-temperature-sensor
) that can measure temperature from 0°C to 50°C and humidity from 20% to 90%.

![](https://github.com/FeliziusV/SmartPod-Hardware-Side/blob/master/Wiki/images/IMG_1803.jpg)


