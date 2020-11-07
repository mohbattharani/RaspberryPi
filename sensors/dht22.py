import os, time
import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

while True:
    h, t = Adafruit_DHT.read_retry (DHT_SENSOR, DHT_PIN)
    print ('Humidity:{0}, Temperature:{1}'.format (h, t))
    time.sleep (10)