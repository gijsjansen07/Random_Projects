#Auto clicking script Minecraft

from time import sleep
from pyautogui import leftClick



x = 1280
y = 720
time = 0

while True:
    leftClick(x,y,3)
    time += 3
    print("click")
    if time == 60 or time > 60:

        break; 


print (" broken")