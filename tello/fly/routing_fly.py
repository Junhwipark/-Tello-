import pygame
from djitellopy import tello
import time

ParkSeungyeon = tello.Tello()
ParkSeungyeon.connect()
print(ParkSeungyeon.get_battery())
time.sleep(2.2)
ParkSeungyeon.takeoff()
speed = 50

time.sleep(5)
ParkSeungyeon.move_forward(150)
time.sleep(5)
ParkSeungyeon.send_rc_control(0, 0, 0, 38)
time.sleep(5)
ParkSeungyeon.move_forward(150)
time.sleep(5)
ParkSeungyeon.send_rc_control(0, 0, 0, 38)
time.sleep(5)
ParkSeungyeon.move_forward(150)
time.sleep(5)
ParkSeungyeon.send_rc_control(0, 0, 0, 38)
time.sleep(5)
ParkSeungyeon.move_forward(150)
time.sleep(5)
ParkSeungyeon.send_rc_control(0, 0, 0, 38)
time.sleep(5)
ParkSeungyeon.send_rc_control(0, 0, 0, 0)
ParkSeungyeon.land()
