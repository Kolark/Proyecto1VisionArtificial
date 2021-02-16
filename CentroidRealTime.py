import cv2

captura = cv2.VideoCapture(0)


def nothing(x):
    pass


cv2.namedWindow('slider')
cv2.createTrackbar('HMax', 'slider', 0, 255, nothing)
cv2.createTrackbar('HMin', 'slider', 0, 255, nothing)
cv2.createTrackbar('VMax', 'slider', 0, 255, nothing)
cv2.createTrackbar('VMin', 'slider', 0, 255, nothing)
cv2.createTrackbar('SMax', 'slider', 0, 255, nothing)
cv2.createTrackbar('SMin', 'slider', 0, 255, nothing)

# Crear el kernel para erosionar y dilatar
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))

while True:
    HMax = cv2.getTrackbarPos('HMax', 'slider')
    HMin = cv2.getTrackbarPos('HMin', 'slider')
    VMax = cv2.getTrackbarPos('VMax', 'slider')
    VMin = cv2.getTrackbarPos('VMin', 'slider')
    SMax = cv2.getTrackbarPos('SMax', 'slider')
    SMin = cv2.getTrackbarPos('SMin', 'slider')

    available, frame = captura.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Blurrear la imagen hsv
    hsvblur = cv2.blur(hsv, (5, 5))

    if available:

        # Crear la máscara con los valores máximos y mínimos del hsv
        # Utilizando el hsv blurreado para mayor presición
        mask = cv2.inRange(hsvblur, (HMin, VMin, SMin), (HMax, VMax, SMax))
        # Utilizar MORPH_OPEN (erosionar -> dilatar) utilizando el kernel
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # Crear imagen en bgr de hsv blurreado
        bgrblur = cv2.cvtColor(hsvblur, cv2.COLOR_HSV2BGR)
        # Crear una imagen en escala de grises del frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Blurrear la imagen en escala de grises
        gray = cv2.blur(gray, (5, 5))
        # Crear una imagen de tres canales de la imagen en escala de grises blurreada
        bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)

        # Separar el fondo del objeto clave
        background = cv2.bitwise_and(bgr, bgr, mask=255-mask)
        selected = cv2.bitwise_and(bgrblur, bgrblur, mask=mask)
        # selected = cv2.bitwise_and(frame, frame, mask=mask)

        # Juntar el fondo en escala de grises y el objeto a color
        output = cv2.add(background, selected)

        # salida = cv2.inRange(hsv, (HMin, VMin, SMin), (HMax, VMax, SMax))
        # ret, thresh = cv2.threshold(salida, 127, 255, 0)

        M = cv2.moments(mask)

        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            cv2.circle(output, (cX, cY), 5, (255, 255, 255), -1)
            cv2.putText(output, "centroid", (cX - 25, cY - 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        except:
            print("Centroid not found")

        cv2.imshow("Frame", frame)
        cv2.imshow("Output", output)
        cv2.imshow("Mask", mask)

    if 0xFF & cv2.waitKey(33) == ord('q'):
        break


cv2.destroyAllWindows()
