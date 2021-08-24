import pyautogui #lies
import time

#get cursor locations
time.sleep(2)
print(pyautogui.position())

#token pos (x=886, y=195)
#package pos (x=1185, y=111)
#post pos (x=849, y=254)

#total slots = post 19 + (inv sqr 9) * (8) = 91 - 9 = 82
#int rots = 91

def autoTurnIn():
    for i in range(82):
        #starting at zavala screen
        pyautogui.click(886, 195) #1st click
        time.sleep(1.2)
        pyautogui.click(886, 195) #2nd click
        time.sleep(1.2)
        pyautogui.click(1185, 111) #package claim
        print("Claiming package #" + str(i) + "\n")

    #Once done, delete on char
    delChar()

def delChar():
    pyautogui.press('f1')
    for i in range(6):
        #primaries
        pyautogui.moveTo(345, 286)
        pyautogui.move(-74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #secondaries
        pyautogui.moveTo(345, 367)
        pyautogui.move(-74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #heavy
        pyautogui.moveTo(345, 449)
        pyautogui.move(-74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #helmet
        pyautogui.moveTo(926, 201)
        pyautogui.move(74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #arms
        pyautogui.moveTo(926, 289)
        pyautogui.move(74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #chest
        pyautogui.moveTo(926, 370)
        pyautogui.move(74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #legs
        pyautogui.moveTo(926, 453)
        pyautogui.move(74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #class
        pyautogui.moveTo(926, 537)
        pyautogui.move(74, 0)
        pyautogui.keyDown('f')
        time.sleep(1.2)
        pyautogui.keyUp('f')
        #log
        print("On inventory rotation #" + str(i))
    #exit inventory
    pyautogui.press('esc')

while True:
    #autoTurnIn()
    delChar()