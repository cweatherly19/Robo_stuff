from bsmLib import RPL
RPL.init()
import curses, time

screen = curses.initscr()
curses.noecho()
curses.halfdelay(1)

elbow_dir = 6
elbow_pul = 5
speed = 500
key = ''
key_hit = time.time()

RPL.pinMode(elbow_pul, RPL.PWM)
RPL.pinMode(elbow_dir, RPL.OUTPUT)
RPL.pinModw(shoulder_pul, RPL.PWM)
RPL.pinMode(shoulder_dir, RPL.OUTPUT)

while key != ord('q'):
    key = screen.getch()
    screen.clear()
    if key == ord('w'):
        screen.addstr('Moving elbow up')
        RPL.digitalWrite(elbow_dir, 0)
        RPL.pwmWrite(elbow_pul, speed, speed * 2)
        key_hit = time.time()
    if key == ord('s'):
        screen.addstr('Moving elbow down')
        RPL.digitalWrite(elbow_dir, 1)
        RPL.pwmWrite(elbow_pul, speed, speed * 2)
        key_hit = time.time()
    if key == ord('o'):
        screen.addstr('Moving shoulder up')
        RPL.digitalWrite(shoulder_dir, 0)
        RPL.pwmWrite(shoulder_pul, speed, speed * 2)
        key_hit = time.time()
    if key == ord('l'):
        screen.addstr('Moving shoulder down')
        RPL.digitalWrite(shoulder_dir, 1)
        RPL.pwmWrite(shoulder_pul, speed, speed * 2)
        key_hit = time.time()
    if time.time() - key_hit > 0.5:
        screen.addstr('Stopped')
        RPL.pwmWrite(elbow_pul, 0, speed * 2)
        RPL.pwmWrite(shoulder_pul, 0, speed * 2)
    if key == ord('q'):
        RPL.pwmWrite(elbow_pul, 0, speed * 2)
        RPL.pwmWrite(shoulder_pul, 0, speed * 2)
        curses.endwin()
