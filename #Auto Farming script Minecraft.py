#Auto clicking script Minecraft
from pynput import keyboard
from pyautogui import leftClick
from time import sleep
x = 1280
y = 720
time_not_pressed = 0 

def on_press(key):

    global time_not_pressed
    time_not_pressed = 0

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
    if key == keyboard.Key.esc:
        # Stop listener             
        return False
    elif time_not_pressed > 20:
        return False
    
    time_not_pressed = 0

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)


listener.start()
while True:
    sleep(1)
    time_not_pressed += 1 
    print(time_not_pressed)
    if time_not_pressed > 20:
        break; 

while time_not_pressed > 20:
    leftClick(x,y,3)
    time_not_pressed+=3
    print(time_not_pressed)
    
print("Program stopped")
