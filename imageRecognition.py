from time import sleep
import pyautogui
from datetime import datetime

#times by 2 because mac weird and thinks it only got half its pixels idk whats going on with it but what ever windows may not multiply by 2 
bagFullCoord = (int(1120 * 2), int(72 * 2))
disconnectCheckCoord = (int(890 * 2), int(630 * 2))
makeHoneyButtonCoord = (int(700 * 2), int(130 * 2))

def isBagFull():
    im = pyautogui.screenshot()
    pixels = im.load()
    
    #for testing if breaks
    #print (pixels[x,y])
    #print(im.size)
    if(pixels[bagFullCoord[0], bagFullCoord[1]][0] > 190): #if red of rgb is greater than 200
        return True
    else:
        return False

    #more testing if breaks
    '''
    for newX in range(x - 50, x + 50):
        for newY in range(y - 50, y + 50):
            pixels[newX, newY] = (0,0,0)
    
    
    #im.save("pixeled", format="png")

    #im.show()'''

def isOnMakeHoneyPlate():
    im = pyautogui.screenshot()
    pixels = im.load()
    if(pixels[makeHoneyButtonCoord[0], makeHoneyButtonCoord[1]] == (238, 238, 242, 255)):
        return True
    else:
        return False
     
def isFacingWrongWay():
    pyautogui.press('o')
    sleep(1)
    pyautogui.press('pagedown')
    sleep(1)
    pyautogui.press('pagedown')
    sleep(1)
    sideCheck = (50 * 2, 1050 * 2)
    sideCheckRGBCheck = (92, 68, 18, 255) #92 might need to be 91

    im = pyautogui.screenshot()
    pixels = im.load()
    pyautogui.press('pageup')
    pyautogui.press('pageup')
    pyautogui.keyUp('fn')
    pixel = pixels[sideCheck[0], sideCheck[1]]
    diff = (pixel[0] - sideCheckRGBCheck[0], pixel[1] - sideCheckRGBCheck[1], pixel[2] - sideCheckRGBCheck[2], 255)
    
    if(diff[0] < 20 and diff[0] > -20 and diff[1] < 20 and diff[1] > -20 and diff[2] < 20 and diff[2] > -20):
        return True
    else:
        return False

def isDisconnected():
    im = pyautogui.screenshot()
    pixels = im.load()
    pixel = pixels[disconnectCheckCoord[0], disconnectCheckCoord[1]]
    if(pixel == (255, 255, 255, 255)):
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print("disconnected at: " + dt_string)
        return True
    return False



def testing():
    
    while True:
        testX = int(50 * 2)
        testY = int(1050 * 2)
        
        im = pyautogui.screenshot()
        pixels = im.load()
        #print(isBagFull())
        print(f"Tested Pixels RGBA is: {pixels[testX, testY]}")
        print(f"Pixels at mouse's RGBA is{pixels[pyautogui.position()[0] * 2, pyautogui.position()[1] * 2]} at a postion of ({pyautogui.position()[0] * 2}, {pyautogui.position()[1] * 2})")
        sleep(1)

if __name__ == "__main__":
    sleep(3)
    
    testing()