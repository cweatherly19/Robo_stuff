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
######################                      ####
#####################         Con_Man        ###
###################### aka The_Weather_Man  ####
#######################                    #####
################################################
################################################

import RoboPiLib as RPL
import setup, time, curses

#setting up the curses file
screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(1)

#to initiate the later while loop
key = ''

#WHEEL SPEEDS
sp1 = 1000
sp2 = 2000

#defining for stop function
key_down = time.time()

#WHEEL PINS
a = 12
b = 13
c = 14
d = 15

#arm pins
s_pin = 1
e_pin = 2
w_pin = 3
g_pin = 4
w_turn = 5

#stop all motors when code starts
RPL.servoWrite(a, 1500)
RPL.servoWrite(b, 1500)
RPL.servoWrite(c, 1500)
RPL.servoWrite(d, 1500)
RPL.servoWrite(w_turn, 0)

#for motor calabration
fraction_shoulder = 16 / 40
fraction_elbow = 24 / 40
fraction_wrist = 20 / 40

#how much each step takes with the arm
step = 1

#kinimatics for the arm test
def test(x, y): #function to test if the arm is in the range of possible motion
    d_three = (y ** 2 + x ** 2) ** 0.5
    if d_three < d_one + d_two or d_three > d_one - d_two:
        return False

#Defining all the movements                                                                                                                                                                    $
def stopall():
    screen.addstr('')
    RPL.servoWrite(a, 1500)
    RPL.servoWrite(b, 1500)
    RPL.servoWrite(c, 1500)
    RPL.servoWrite(d, 1500)
    RPL.servoWrite(w_turn, 0)

def turnRight():
    screen.addstr('')
    RPL.servoWrite(a, sp1)
    RPL.servoWrite(b, sp1)
    RPL.servoWrite(c, sp1)
    RPL.servoWrite(d, sp1)

def turnLeft():
    screen.addstr('')
    RPL.servoWrite(a, sp2)
    RPL.servoWrite(b, sp2)
    RPL.servoWrite(c, sp2)
    RPL.servoWrite(d, sp2)

def goForwards():
    screen.addstr('')
    RPL.servoWrite(a, sp2)
    RPL.servoWrite(b, sp2)
    RPL.servoWrite(c, sp1)
    RPL.servoWrite(d, sp1)

def goBackwards():
    screen.addstr('')
    RPL.servoWrite(a, sp1)
    RPL.servoWrite(b, sp1)
    RPL.servoWrite(c, sp2)
    RPL.servoWrite(d, sp2)

def leftForwards():
    screen.addstr('')
    RPL.servoWrite(a, sp2)
    RPL.servoWrite(b, sp2)
    RPL.servoWrite(c, 1500)
    RPL.servoWrite(d, 1500)

def leftBackwards():
    screen.addstr('')
    RPL.servoWrite(a, sp1)
    RPL.servoWrite(b, sp1)
    RPL.servoWrite(c, 1500)
    RPL.servoWrite(d, 1500)

def rightForwards():
    screen.addstr('')
    RPL.servoWrite(a, 1500)
    RPL.servoWrite(b, 1500)
    RPL.servoWrite(c, sp1)
    RPL.servoWrite(d, sp1)

def rightBackwards():
    screen.addstr('')
    RPL.servoWrite(a, 1500)
    RPL.servoWrite(b, 1500)
    RPL.servoWrite(c, sp2)
    RPL.servoWrite(d, sp2)

while key != ord('f'):
    #read keys and clear screen
    key = screen.getch()
    screen.clear()

    if key == ord('w'):
        screen.addstr('Forwards')
        goForwards()
        key_down = time.time()

    if key == ord('s'):
        screen.addstr('Backwards')
        goBackwards()
        key_down = time.time()

    if key == ord('a'):
        screen.addstr('Left 180')
        turnLeft()
        key_down = time.time()

    if key == ord('d'):
        screen.addstr('Right 180')
        turnRight()
        key_down = time.time()

    if key == ord('q'):
        screen.addstr('Left Forwards')
        leftForwards()
        key_down = time.time()

    if key == ord('e'):
        screen.addstr('Right Forwards')
        rightForwards()
        key_down = time.time()

    if key == ord('z'):
        screen.addstr('Left Backwards')
        leftBackwards()
        key_down = time.time()

    if key == ord('c'):
        screen.addstr('Right Backwards')
        rightBackwards()
        key_down = time.time()

    if key == ord('x'):
        screen.addstr('Safe Fail Stop')
        stopall()
        key_down = time.time()

    if key == ord('i'):
        screen.addstr('Raising Arm')
        y += step
        if test(x, y) == False:
            y -= step

    if key == ord('k'):
        screen.addstr('Dropping Arm')
        y -= step
        if test(x, y) == False:
            y += step

    if key == ord('j'):
        screen.addstr('Retracting Arm')
        y -= step
        if test(x, y) == False:
            y += step

    if key == ord('l'):
        screen.addstr('Extending Arm')
        y += step
        if test(x, y) == False:
            y -= step

    if key == ord('n'):
        screen.addstr('Wrist Up')
        wrist_movement += step / math.pi

    if key == ord('m'):
        screen.addstr('Wrist Down')
        wrist_movement -= step / math.pi

    if key == ord('u'):
        screen.addstr('Rotate Clockwise')
        RPL.servoWrite(w_turn, 2000)
        key_down = time.time()

    if key == ord('o');
        screen.addstr('Rotate Counterclockwise')
        RPL.servoWrite(w_turn, 1000)
        key_down = time.time()

    if key == ord('1'):
        screen.addstr('Grasper Closed')
        RPL.servoWrite(g_pin, 1000)

    if key == ord('2'):
        screen.addstr('Grasper Opened')
        RPL.servoWrite(g_pin, 1500)

    if time.time() - key_down > 0.1:
        screen.addstr('Stopped')
        stopall()

    #close out of curses without any errors
    if key == ord('f'):
        stopall()
        curses.endwin()

    #doing the math for the kinimatics
    if test(x, y) != False:
        try:
            a_elbow = math.acos(round((d_one ** 2 + d_two ** 2 - y ** 2 - x ** 2) / (2 * d_one * d_two), 1))
            a_shoulder = math.asin(round((d_two * math.sin(a_elbow) / (y ** 2 + x ** 2) ** 0.5), 1)) + math.atan2(y, x) #calculate all angle values
        except:
            a_elbow = 0; a_shoulder = math.pi

        a_wrist = math.arcsin(round(y * sin(y / (x ** 2 + y ** 2) ** 0.5) / x, 1)) + wrist_movement

        input_elbow = int(fraction_elbow * a_elbow * 2000 / math.pi + 400)
        input_shoulder = int(fraction_shoulder * a_shoulder * 2000 / math.pi + 400) #angle and motor value calculations
        input_wrist = int(fraction_wrist * a_wrist * 2000 / math.pi + 400)

        if input_wrist > 3000:
            input_wrist = 3000
            wrist_movement -= step
        if input_wrist < 0:
            input_wrist = 0
            wrist_movement += step

        #moving the motors to their positions
        RPL.servoWrite(s_pin, input_shoulder)
        RPL.servoWrite(e_pin, input_elbow) #to move the motors
        RPL.servoWrite(w_pin, input_wrist)

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
#######################                     ####
#####################        Con_Man         ###
###################### aka The_Weather_Man  ####
#######################                    #####
################################################
################################################
