import RPi.GPIO as GPIO
import datetime
import time

def water_plants():
    pinPump = 4
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pinPump, GPIO.OUT)
    GPIO.output(pinPump, GPIO.HIGH)
    time.sleep(12)
    GPIO.output(pinPump, GPIO.LOW)
    with open("/home/user/WateringStats.txt", "a") as f:
        f.write(f"{datetime.datetime.now()}: ¡La planta se regó!\n\n")
    GPIO.cleanup()

water_plants()
