import RPi.GPIO as GPIO
import time 

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

n = 10
p = GPIO.PWM(24, 1000)
p.start(0)

try:
    while True:
        f= int(input())
        p.ChangeDutyCycle(f)
        print(3.3*f/100)
finally:
    p.stop()
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")