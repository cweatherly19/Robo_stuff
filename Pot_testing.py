import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi
import time
import math

elbow_range = 775 #range of read values by elbow POT
shoulder_range = 840 #range of read values by shoulder POT

pot_pin_elbow = 6
pot_pin_shoulder = 7

print "Output given in degrees"
print "Elbow pin:", pot_pin_elbow
print "Shoulder pin:", pot_pin_shoulder
time.sleep(3)

while True:
  pot_value_elbow = RPL.analogRead(pot_pin_elbow)
  pot_value_shoulder = RPL.analogRead(pot_pin_shoulder)
  print(pot_value_elbow * 270 / elbow_range - 45) #to only use 180 degrees of the POT's range
  print(pot_value_elbow * 3 * math.pi / (2 * elbow_range) - math.pi / 4)
  time.sleep(0.1)
  print(pot_value_shoulder * 270 / shoulder_range - 45) #to only use 180 degrees of the POT's range
  print(pot_value_shoulder * 3 * math.pi / (2 * shoulder_range) - math.pi / 4)
  time.sleep(0.1)
