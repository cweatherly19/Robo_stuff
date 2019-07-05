################################################
################################################
####                      ######################
### THIS MEME WAS MADE BY  #####################
####                      ######################
################################################
################################################
######################                     #####
#####################  XxX_The_SIXXX_S4ges  ####
######################                     #####
################################################
################################################

################################################
################### IMPORT #####################
################################################
import RoboPiLib as RPL
import setup, time
import sys, tty, termios, signal, curses

################################################
################### PREREQ #####################
################################################
screen = curses.initscr()
curses.noekeyo()
curses.cbreak()
curses.halfdelay(1)

key = ''

time.sleep(2)
old_settings = termios.tcgetattr(sys.stdin.fileno()) #records current terminal settings
signal.signal(signal.SIGALRM, interrupted) #calls interrupted when alarm stops
tty.setraw(sys.stdin.fileno()) #raw keystroke input, keyanges terminal settings

################################################
#################### VARS ######################
################################################

#LAZY SUZAN AND WRIST SPINNER SPEEDS
d1 = 1000
d2 = 2000

#WHEEL SPEEDS
sp1 = 1000
sp2 = 2000

#WHEEL PINS
a = 12
b = 13
c = 14
d = 15

#ARM PINS
e = 0
f = 1
g = 2
h = 3
i = 4
j = 5

#STOP CONTINUOUS ROTATION
crstop = 1500

#----SYNkeyRONIZES MOTORS

#--STANDARD

#JOINT 1
aj1 = int(1000)
#JOINT 2
aj2 = int(1000)
#JOINT 3
aj3 = int(1000)
#ACTUATOR
aac = int(1000)

#--CONTINUOUS ROTATION
RPL.servoWrite(a,crstop)
RPL.servoWrite(b,crstop)
RPL.servoWrite(c,crstop)
RPL.servoWrite(d,crstop)
print "synkeyronized"

################################################
################## FUNCTION ####################
################################################

#STANDARD SERVOS
def regulate(pin):
 if pin > 3000:
   pin = 3000
 if pin < 0:
   pin = 10
 return pin

def stopall():
 RPL.servoWrite(a,1500)
 RPL.servoWrite(b,1500)
 RPL.servoWrite(c,1500)
 RPL.servoWrite(d,1500)
 RPL.servoWrite(i,0)
 RPL.servoWrite(j,0)


def interrupted(signum,frame):
   print("interrupted")

def wasddrive(p1,p2,p3,p4,spd1,spd2):
   screen.addstr('')
   RPL.servoWrite(p1,spd1)
   RPL.servoWrite(p2,spd1)
   RPL.servoWrite(p3,spd2)
   RPL.servoWrite(p4,spd2)

################################################
#################### LOOP ######################
################################################

while key != ord('f'):
    key = screen.getkey()
    screen.clear()

    if key == ord('w'):
    	wasddrive(a,b,c,d,sp1,sp2)
        screen.addstr('Forwards')
        key_down = time.time()

    if key == ord('s'):
        screen.addstr('Backwards')
        wasddrive(a,b,c,d,sp2,sp1)
        key_down = time.time()

    if key == ord('a'):
        screen.addstr('Left 180')
        wasddrive(a,b,c,d,sp2,sp2)
        key_down = time.time()

    if key == ord('d'):
        screen.addstr('Right 180')
        wasddrive(a,b,c,d,sp1,sp1)
        key_down = time.time()

    if key == ord('q'):
        screen.addstr('Left Forwards')
        wasddrive(a,b,c,d,crstop,sp2)
        key_down = time.time()

    if key == ord('e'):
        screen.addstr('Right Forwards')
        wasddrive(a,b,c,d,sp1,crstop)
        key_down = time.time()

    if key == ord('z'):
        screen.addstr('Left Backwards')
        wasddrive(a,b,c,d,crstop,sp1)
        key_down = time.time()

    if key == ord('c'):
        screen.addstr('Right Backwards')
        wasddrive(a,b,c,d,sp2,crstop)
        key_down = time.time()

    if key == ord('x'):
        screen.addstr('Safe Fail Stop')
        stopall()
        key_down = time.time()

    if time.time() - key_down > 0.1:
        screen.addstr('Stopped')
        stopall()

    if key == ord('f'):
        stopall()
        curses.endwin()

	#HAND
	elif key == ord('t'):
		screen.addstr('Closing Hand')
		stopall()
		aac -= 10
		key_down = time.time()
	elif key == ord('g'):
		screen.addstr('Opening Hand')
		stopall()
		aac += 10
		key_down = time.time()

	#BASE
	elif key == ord('y'):
		screen.addstr('Joint 1 Up')
		stopall()
		aj1 +=10
		key_down = time.time()
	elif key == ord('h'):
		screen.addstr('Joint 1 Down')
		aj1 -=10
		stopall()
		key_down = time.time()

	#JOINT 1
	elif key == ord('u'):
		screen.addstr('Joint 2 Down')
		aj2 -=10
		stopall()
		key_down = time.time()
	elif key == ord('j'):
		screen.addstr('Joint 1 Up')
		aj2 +=10
		stopall()
		key_down = time.time()


	#JOINT 2
	elif key == ord('i'):
		screen.addstr('Joint 1 Up')
		aj3 +=10
		stopall()
		key_down = time.time()
	elif key == ord('k'):
		screen.addstr('Joint 1 Down')
		aj3 -=10
		stopall()
		key_down = time.time()

	#ROTATE HAND
	elif key == ord('o'):
		screen.addstr('Rotating Hand')
		RPL.servoWrite(j,1000)
		key_down = time.time()
	elif key == ord('l'):
		screen.addstr('Rotating Hand')
		RPL.servoWrite(j,2000)
		key_down = time.time()

	#LAZY SUZAN
	elif key == ord('p'):
		screen.addstr('Lazy Suzan')
		RPL.servoWrite(i,1000)
		key_down = time.time()
	elif key == ord(';'):
		screen.addstr('Lazy Suzan')
		RPL.servoWrite(i,2000)
		key_down = time.time()

#THIS REGULATES THE CLAW SO IT DOESN'T BREAK SHIT
 if aac >1500:
   aac = 1500
 if aac <1000:
   aac = 1000
#LETS YOU KNOW HOW OPEN THE CLAW IS
 print str(aac)
#WRITES ALL OF THE STANDARD SERVOS
 RPL.servoWrite(e,aac)
 RPL.servoWrite(f,regulate(aj1))
 RPL.servoWrite(g,regulate(aj2))
 RPL.servoWrite(h,regulate(aj3))



################################################
################################################
####                      ######################
### THIS MEME WAS MADE BY  #####################
####                      ######################
################################################
################################################
######################                     #####
#####################  XxX_The_SIXXX_S4ges  ####
######################                     #####
################################################
################################################
