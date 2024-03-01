import RPi.GPIO as GPIO
import time

dac    = [8, 11, 7, 1, 0, 5, 12, 6]
number = [1,  0, 1, 1, 0, 0,  0, 1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

bin0   = [0, 0, 0, 0, 0, 0, 0, 0]
bin2   = [0, 0, 0, 0, 0, 0, 1, 0]
bin5   = [0, 0, 0, 0, 0, 1, 0, 1]
bin32  = [0, 0, 1, 0, 0, 0, 0, 0]
bin64  = [0, 1, 0, 0, 0, 0, 0, 0]
bin127 = [0, 1, 1, 1, 1, 1, 1, 1]
bin255 = [1, 1, 1, 1, 1, 1, 1, 1]
bin256 = [0, 0, 0, 0, 0, 0, 0, 0]

GPIO.output(dac, bin2)
time.sleep(5)

GPIO.output(dac, bin0)
time.sleep(15)
GPIO.output(dac, bin2)
time.sleep(15)
GPIO.output(dac, bin5)
time.sleep(15)
GPIO.output(dac, bin32)
time.sleep(15)
GPIO.output(dac, bin64)
time.sleep(15)
GPIO.output(dac, bin127)
time.sleep(15)
GPIO.output(dac, bin255)
time.sleep(15)
GPIO.output(dac, bin256)
time.sleep(15)

GPIO.output(dac, 0)
GPIO.cleanup()

