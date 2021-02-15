import cv2

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
    disponible, fotograma = captura.read()
    hsv = cv2.cvtColor(fotograma,cv2.COLOR_BGR2HSV)
    if disponible == True:
        salida = cv2.inRange(hsv,(HMin,VMin,SMin),(HMax,VMax,SMax))
        ret,thresh = cv2.threshold(salida,127,255,0)

        M = cv2.moments(thresh)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(salida, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(salida, "centroid", (cX - 25, cY - 25),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            print("Centroid not found")
        
        
        cv2.imshow("Og",fotograma)
        cv2.imshow("Resultado",salida)
    ch = 0xFF & cv2.waitKey(33)
    if ch == ord('q'):
        break

cv2.destroyAllWindows()