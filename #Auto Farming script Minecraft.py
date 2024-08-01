#Auto clicking script Minecraft
from pynput import keyboard
from pyautogui import leftClick
from time import sleep
x = 1280
y = 720
time_not_pressed = 0 
on = True
def on_press(key):



    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):

    global time_not_pressed
    
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc or time_not_pressed >= 20:
        # Stop listener       
        global on    
        on = False      
        return False
   
    
    time_not_pressed = 0

# ...or, in a non-blocking fashion: 
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


listener.start()
while  True:
    if on == False:
        break; 

    if time_not_pressed < 21 :
        sleep(1)
        time_not_pressed += 1 
        print(time_not_pressed)
    

    if time_not_pressed > 20:
        leftClick(x,y,3)
        time_not_pressed+=3
        print(time_not_pressed)
    
print("Program stopped")
