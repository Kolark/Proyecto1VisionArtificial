import cv2
import Clases
captura = cv2.VideoCapture(0)
chars = Clases.Tools.Characteristics()

def nothing(x):
    pass
cv2.namedWindow('slider')
cv2.createTrackbar('HMax','slider',0,255,nothing)
cv2.createTrackbar('HMin','slider',0,255,nothing)
cv2.createTrackbar('VMax','slider',0,255,nothing)
cv2.createTrackbar('VMin','slider',0,255,nothing)
cv2.createTrackbar('SMax','slider',0,255,nothing)
cv2.createTrackbar('SMin','slider',0,255,nothing)

while(True):

    HMax = cv2.getTrackbarPos('HMax','slider')
    HMin = cv2.getTrackbarPos('HMin','slider')
    VMax = cv2.getTrackbarPos('VMax','slider')
    VMin = cv2.getTrackbarPos('VMin','slider')
    SMax = cv2.getTrackbarPos('SMax','slider')
    SMin = cv2.getTrackbarPos('SMin','slider')
    
    segmentation = Clases.Segmentation.Segmentation(HMin,VMin,SMin,HMax,VMax,SMax)
    disponible, fotograma = captura.read()
    segmentedImage = segmentation.segmentate(fotograma)
    if disponible == True:
        posX,posY,imagentxt = chars.findCentroid(segmentedImage)
        cv2.imshow("ConTexto",imagentxt)
        cv2.imshow("Og",fotograma)
        cv2.imshow("Segmentado",segmentedImage)
    ch = 0xFF & cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()