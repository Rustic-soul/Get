import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)


def decimal_to_binary_list(number):
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
        num = int(input("Введите число от 0 до 255: "))
        try:
            if 0 <= num <= 255:
                print("Напряжение: ", end=' ')
                print((3.3 / 256) * num, end='\n')
                GPIO.output(dac, decimal_to_binary_list(num))
            else:
                if (num < 0) or (num > 255):
                    print("Введены неккоректные данные")
        except Exception:
            if num == "q": break
            print("Введите число, не строку")
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
