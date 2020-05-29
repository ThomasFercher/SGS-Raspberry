import pyrebase
import time
from datetime import datetime
from decimal import Decimal
import json
from json import encoder
import Adafruit_DHT

#Firebase Init

config = {     
  "apiKey": "AIzaSyAeTF-VH5vxA0-ssHg4rMcjIodzBnnPvPw",
  "authDomain": "smartgrowsystem-sgs.firebaseapp.com",
  "databaseURL": "https://smartgrowsystem-sgs.firebaseio.com/",
  "storageBucket": "smartgrowsystem-sgs.appspot.com"
}

firebase = pyrebase.initialize_app(config)  
db = firebase.database()

#DHT22

sensor = Adafruit_DHT.DHT22
pin = '4'

#Main Loop

while(True):
    #get timestamp
    ts = datetime.now()
    
    #get sensor data
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    
    #format data
    formathumidity = '%.2f'%humidity
    formattemperature = '%.2f'%temperature
	
    #set sensor data in firebase
    #temperature
    db.child("temperature").set(formattemperature)
    db.child("temperatures").child(ts.strftime("%Y-%m-%d %H:%M:%S")).set(formattemperature)
    #humidity
    db.child("humidity").set(formathumidity)
    db.child("humiditys").child(ts.strftime("%Y-%m-%d %H:%M:%S")).set(formathumidity)
    
    #interval timing
    time.sleep(3)
