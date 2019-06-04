Reckoning_list = [] #defining a list to use later
apple = microsoft = quit = False #set all variables to not read until called
print "Input your list, then hit '1':"

try: #if running on apple
    import sys, tty, termios #imports for no return command
    fd = sys.stdin.fileno() #unix file descriptor to define the file type
    old_settings = termios.tcgetattr(fd) #records the existing console settings
    tty.setcbreak(sys.stdin) #sets the style of input
    apple = True #computer type

except: #if running on microsoft
    import msvcrt #microsoft file for key input
    microsoft = True #computer typeprint "Input your list, then hit '1' to replay your list:"

while quit == False:
    if microsoft == True:
        key = msvcrt.getch() #format the keys into readable characters
    elif apple == True:
        key = sys.stdin.read(1) #reads one character of input without requiring a return command

    for i in range(0, 1): #only records one step
        Reckoning_list.insert(i, key.upper())
        if '1' in Reckoning_list and quit == False:
            if apple == True:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #resets the console settings
            Reckoning_list.remove('1')
            quit = True

print 'Display list forward or in reverse? [F, R]'
while True:
    if microsoft == True:
        key = msvcrt.getch() #format the keys into readable characters
    if apple == True:
        key = sys.stdin.read(1) #reads one character of input without requiring a return command
    if key.upper() == 'F':
        print 'Forward:'
        print Reckoning_list[::-1]
        break
    if key.upper() == 'R':
        print 'Reverse:'
        print Reckoning_list[:]
        break
