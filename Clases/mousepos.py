import numpy as np
import cv2 as cv
import mouse
import win32api,win32con
import keyboard
# win32api.SetCursorPos((x,y))
#SCREEN SIZE
# ix,iy = 640,480

# mouse callback function
def click_mouse(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDOWN:
        posX,posY = normMousePos(x,y)
        print("x: " + str(posX))
        print("y: " + str(posY))
        
def MoveMouse(posX,width,posY,height):
    px,py = normMousePos(posX,width,posY,height)
    px=px-0.5
    py=py-0.5
    py*=-1
    # print(f"px:{px},py:{py}")
    nx = px*1920*(int(65535*2)/win32api.GetSystemMetrics(0))#+ int(65535/2)
    ny = py*1080*(int(65535*2)/win32api.GetSystemMetrics(1))#+ int(65535/2)

    # print(f"x:{nx},y:{ny}")
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE|win32con.MOUSEEVENTF_MOVE,int(nx),int(ny))
    # win32api.SetCursorPos((int(px*1920),int(py*1080)))
    # mouse.move(px*1920,py*1080)

class inputStates:
    def __init__(self):
        self.canSendInput = False
    def EvalInputs(self,posX,width,posY,height,up,down,left,right,radius):

        isInDeadZone = self.CheckIfDeadZone(posX,posY,width,height,radius)
        if isInDeadZone:
            self.canSendInput = True

        vertical = self.CheckVertical(posY,height,up,down)
        horizontal = self.CheckHorizontal(posX,width,left,right)
        if self.canSendInput:
            if vertical > 0:
                print("UP")
                keyboard.press('up')
                keyboard.release('up')      
                self.canSendInput = False
                return
            elif vertical < 0:
                print("DOWN")
                keyboard.press('down')
                keyboard.release('down')  
                self.canSendInput = False
                return
            if horizontal > 0:
                print("RIGHT")
                keyboard.press('right')
                keyboard.release('right')  
                self.canSendInput = False
                return
            elif horizontal<0:
                print("LEFT")
                keyboard.press('left')
                keyboard.release('left')  
                self.canSendInput = False
                return

            

    def CheckIfDeadZone(self,posX,posY,width,height,radius):
        cx = width//2
        cy = height//2
        distance = np.sqrt((posX-cx)**2 + (posY-cy)**2)
        if distance < radius:
            return True
        else:
            return False

    def CheckVertical(self,posY,height,up,down):
        if posY < up:
            return 1
        elif posY > (height-down):
            return -1
        else:
            return 0


    def CheckHorizontal(self,posX,width,left,right):
        if posX < left:
            return -1
        elif posX > (width-right):
            return 1
        else:
            return 0



def normMousePos(x,width,y,height):
    # return x/width,y/height
    return x/width,y/height
