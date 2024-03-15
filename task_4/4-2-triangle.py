import RPi.GPIO as GPIO
import time 

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def dec2bin(number):
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        number = number // 2
    while len(binary_list) < 8:
        binary_list.insert(0, 0)
    return binary_list

try:
    while True:
        per = int(input("Введите период: "))
        while True:
            i = 0
            while i < 256:
                GPIO.output(dac, dec2bin(i))
                time.sleep(per / 512)
                i += 1
            i -= 1

            while i >= 0:
                GPIO.output(dac, dec2bin(i))
                time.sleep(per / 512)
                i -= 1
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")