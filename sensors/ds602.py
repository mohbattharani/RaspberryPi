# $ sudo pip3 install adafruit-blinka

import time, board, digitalio

pir_sensor = digitalio.DigitalInOut (board.D4)
pir_sensor.direction = digitalio.Direction.INPUT

while True:
    print (pir_sensor.value)
    time.sleep (5)