import pyautogui

pyautogui.moveTo(991, 20, 2)

#If you want the mouse to gradually move to the new location, pass a third argument for the duration (in seconds) the movement should take.
pyautogui.moveTo(329, 347, 2, pyautogui.easeInElastic)

#Obs: By default, pyautogui.MINIMUM_DURATION is 0.1

pyautogui.move(0, 309) #desce 300 pixels a partir do ponto que ele parou em moveTo

#----------------------------------------------------------------------------------------
#PyAutoGUI’s dragTo() and drag() functions have similar parameters as the moveTo() and move() functions. 
# In addition, they have a button keyword which can be set to 'left', 'middle', and 'right'

pyautogui.dragTo(360, 103, button='right')


