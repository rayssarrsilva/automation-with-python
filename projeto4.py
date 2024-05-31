import pyautogui
#PyAutoGUI 
# documentaçao:     https://pyautogui.readthedocs.io/en/latest/mouse.html

#resoluçao da tela em tupla
print(pyautogui.size())

#The current X and Y coordinates of the mouse cursor
print(pyautogui.position())


#Print constantly, the position of the mouse cursor
print('Press Ctrl-C to quit. responsavel: KeyboardInterrupt')
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')

# moveTo() function move the mouse cursor to the X and Y integer coordinates you pass it

#pyautogui.moveTo(991, 20)