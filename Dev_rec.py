Reckoning_list = [] #defining a list to use later
Inverse_list = []
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
    microsoft = True #computer typeprint

while quit == False:
    if microsoft == True:
        key = msvcrt.getch() #format the keys into readable characters
    elif apple == True:
        key = sys.stdin.read(1) #reads one character of input without requiring a return command

#############################################################################################
######### Create the initial input list
#############################################################################################

    for i in range(0, 1): #only records one step
        Reckoning_list.insert(i, key.upper())
        if '1' in Reckoning_list and quit == False:
            Reckoning_list.remove('1')

#############################################################################################
######### Create the inverse list
#############################################################################################

    if ('W' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'S')
    if ('S' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'W')
    if ('A' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'D')
    if ('D' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'A')

##############################################################################################

    if key == '1': #quit when the '1' key is pressed
        if apple == True:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #resets the console settings
        quit = True

print Reckoning_list

del Inverse_list[0] #the first term coppies twice, so you remove one of them
print Inverse_list
