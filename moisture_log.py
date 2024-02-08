import RPi.GPIO as GPIO
import datetime
import spidev
import time

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 1000000

def readData(channel):
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    data = ((adc[1] & 3) << 8) + adc[2]
    return data

def log_moisture():
    moisture = readData(0)
    currentTime = datetime.datetime.now()
    with open("/home/user/HumidityStats.txt", "a") as f:
        f.write(f"{currentTime}:\n")
        f.write(f"Humedad actual: {round((moisture - 330) / 450 * 100, 2)}% ({moisture})\n\n")

log_moisture()
