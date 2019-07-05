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
################################################
################################################
import RoboPiLib as RPL
import setup, time, curses
#import time, curses

screen = curses.initscr()
curses.noecho()
curses.cbreak()
curses.halfdelay(1)

key = ''

#WHEEL SPEEDS
sp1 = 1000
sp2 = 2000

key_down = time.time()

#WHEEL PINS
a = 12
b = 13
c = 14
d = 15

RPL.servoWrite(a, 1500)
RPL.servoWrite(b, 1500)
RPL.servoWrite(c, 1500)
RPL.servoWrite(d, 1500)

#Stops wheels                                                                                                                                                                    $
def stopall():
    screen.addstr('')
    RPL.servoWrite(a, 1500)
    RPL.servoWrite(b, 1500)
    RPL.servoWrite(c, 1500)
    RPL.servoWrite(d, 1500)

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

    if time.time() - key_down > 0.1:
        screen.addstr('Stopped')
        stopall()

    if key == ord('f'):
        stopall()
        curses.endwin()


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
################################################
################################################
