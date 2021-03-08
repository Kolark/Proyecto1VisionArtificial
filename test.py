import cv2
import Clases
captura = cv2.VideoCapture(0)

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
    
    segmentation = Clases.segmentation.Segmentation(HMin,SMin,VMin,HMax,SMax,VMax)
    disponible, fotograma = captura.read()
    segmentedImage = segmentation.segmentate(fotograma)
    if disponible == True:
        posX,posY,msg = Clases.tools.Characteristics.findCentroid(segmentedImage)
        # cv2.imshow("ConTexto",imagentxt)
        cv2.circle(fotograma, (int(posX), int(posY)), 5, (255, 255, 255), -1)
        cv2.putText(fotograma, msg, (int(posX) - 25, int(posY) - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.imshow("Og",fotograma)
        cv2.imshow("Segmentado",segmentedImage)
    ch = 0xFF & cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()