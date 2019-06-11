import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi
import time

elbow_range = 775 #range of read values by elbow POT
shoulder_range = 825 #range of read values by shoulder POT

pot_pin_elbow = 6
pot_pin_shoulder = 7

print "Output given in degrees"
print "Elbow pin:", pot_pin_elbow
print "Shoulder pin:", pot_pin_shoulder
time.sleep(5)

while True:
  pot_value_elbow = RPL.analogRead(pot_pin_elbow)
  pot_value_shoulder = RPL.analogRead(pot_pin_shoulder)
  print(pot_value_elbow * 270 / elbow_range)
  time.sleep(0.05)
  print(pot_value_shoulder * 270 / shoulder_range)
  time.sleep(0.05)
