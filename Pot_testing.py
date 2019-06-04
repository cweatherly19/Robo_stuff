import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi
import time

motor_pin = 8

while True:
  pot_value = RPL.analogRead(motor_pin)
  print pot_value
  time.sleep(0.5)
