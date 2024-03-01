import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
list_pin = [2, 3, 4, 17, 27, 22, 10, 9]

GPIO.setup(list_pin, GPIO.OUT)

for j in range(3):
    for i in list_pin:
        GPIO.output(i, 1)
        time.sleep(0.2)
        GPIO.output(i, 0)

GPIO.output(list_pin, 1)
time.sleep(1)
GPIO.output(list_pin, 0)
GPIO.cleanup()
        