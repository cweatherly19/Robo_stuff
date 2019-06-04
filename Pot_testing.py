import RoboPiLib_pwm as RPL #to pull all files needed to run the motors
RPL.RoboPiInit("/dev/ttyAMA0", 115200) #connect to RoboPi

motor_pin = 8

while True:
  pot_value = RPL.analogRead(motor_pin)
  try:
    print RPL.digitalRead(motor_pin)
  except:
    print pot_value
