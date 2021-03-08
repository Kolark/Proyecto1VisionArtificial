import numpy as np
import cv2 as cv
import mouse
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
    mouse.move(px*1920,py*1080)

def normMousePos(x,width,y,height):
    # return x/width,y/height
    return x/width,y/height
#print in screen the values of the mouse position
# def print_value(x,y,vx,vy):
#     position= 'x:'+ str(round(vx,nd)) + ', y:' + str(round(vy,2))
#     cv.putText(img, position, (x,y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 1)
    
        
# Create a black image, a window and bind the function to window


# img = np.zeros((iy,ix,3), np.uint8)
# cv.namedWindow('image')
# cv.setMouseCallback('image',click_mouse)
# while(1):
#     cv.imshow('image',img)
#     ch=0xFF & cv.waitKey()
#     if ch==ord('q'):
#         break
# cv.destroyAllWindows()