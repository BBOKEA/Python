import serial
import sys
import time
import threading
import queue


ser = serial.Serial('COM5', 9600) #아두이노 포트 할당

from serial import Serial
print("아두이노 통신 시작")

while True:
    line = ser.readline().decode("utf-8")
    print(line)