import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(dac, GPIO.out)


def decimal_to_binary_list(number):
    binary_list = []
    while number > 0:
        remainder = number % 2
        binary_list.insert(0, remainder)
        number = number // 2
    return binary_list


try:
    while True:
        print("Введите число: ")
        tmp = int(input())
        GPIO.output(dac, decimal_to_binary_list(tmp))
        print("Напряжение: ")
        print((3.3 / 256) * tmp, end='\n')
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
