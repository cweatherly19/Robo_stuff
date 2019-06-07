Reckoning_list = [] #defining a list to use later
Inverse_list = []
apple = microsoft = quit = False #set all variables to not read until called
print "Input your list using the [W, A, S, D, Q, E, Z, X] keys, then hit '1':"

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

#############################################################################################
######### Create the inverse list
#############################################################################################

    if key.upper() == 'A':
    #if ('W' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'S')
    if key.upper() == 'S':
    #if ('S' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'W')
    if key.upper() == 'A':
    #if ('A' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'D')
    if key.upper() == 'D':
    #if ('D' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'A')
    if key.upper() == 'Q':
    #if ('Q' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'E')
    if key.upper() == 'E':
    #if ('E' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'Q')
    if key.upper() == 'Z':
    #if ('Z' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'X')
    if key.upper() == 'X':
    #if ('X' in Reckoning_list[i]) == True:
        Inverse_list.insert(i, 'Z')

    if (Reckoning_list[i] in ['W', 'A', 'S', 'D', 'Q', 'E', 'Z', 'X']) == False: #any unprogrammed inputs are deleted
        del Reckoning_list[i]

##############################################################################################

    if key == '1': #quit when the '1' key is pressed
        if apple == True:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) #resets the console settings
        quit = True

if len(Inverse_list) > 0:
    print Reckoning_list
    print Inverse_list
else:
    print 'No valid list input'
