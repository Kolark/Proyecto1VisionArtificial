import cv2
import numpy as np
import keyboard

from clases.tools import Characteristics


LEFT = 0
RIGHT = 1

WIDTH = HEIGHT = 0

LEFT_PORCENT = RIGHT_PORCENT = 40
BOTTON_PORCENT = 35


last_side = None


camera = cv2.VideoCapture(0)

# Start
available, frame = camera.read()

if available:
    HEIGHT, WIDTH, _ = frame.shape


# Update
while True:
    available, frame = camera.read()

    if not available:
        print("Cámara no disponible")
        break

    frame = cv2.flip(frame, 1)

    # Límite izquierdo
    cv2.line(frame, (LEFT_PORCENT * WIDTH // 100, 0),
             (LEFT_PORCENT * WIDTH // 100, HEIGHT), (0, 0, 0), 3)
    # Límite derecho
    cv2.line(frame, (WIDTH - RIGHT_PORCENT *
                     WIDTH // 100, 0), (WIDTH - RIGHT_PORCENT *
                                        WIDTH // 100, HEIGHT), (0, 0, 0), 3)
    # Límite inferior
    cv2.line(frame, (0, HEIGHT - BOTTON_PORCENT * HEIGHT // 100),
             (WIDTH, HEIGHT - BOTTON_PORCENT * HEIGHT // 100), (0, 0, 0), 3)

    # Convertirlo a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x, y, w, h, face_found = Characteristics.find_face(gray)

    # Recuadro de la cara
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 2)

    center = ((x + w//2), (y + h//2))

    # Si no encontró un rostro
    if not face_found:
        print('face not found')
    # Si encontró un rostro
    else:
        # Si tiene el rostro en el centro
        if center[0] > LEFT_PORCENT * WIDTH // 100 and \
                center[0] < WIDTH - RIGHT_PORCENT * WIDTH // 100 and \
                center[1] < HEIGHT - BOTTON_PORCENT * HEIGHT // 100:
            print('center')
            keyboard.release('left')
            keyboard.release('right')
            keyboard.release('space')

        # Si tiene el rostro en la parte inferior
        elif center[1] > HEIGHT - BOTTON_PORCENT * HEIGHT // 100:
            print('inferior')
            if last_side == LEFT:
                keyboard.press('left')
                keyboard.release('right')
            elif last_side == RIGHT:
                keyboard.press('right')
                keyboard.release('left')

            keyboard.press('space')

        # Si tiene el rostro en la parte izquierda
        elif center[0] < LEFT_PORCENT * WIDTH // 100:
            print('left')
            last_side = LEFT

            keyboard.press('left')
            keyboard.release('space')

        # Si tiene el rostro en la parte derecha
        elif center[0] > WIDTH - RIGHT_PORCENT * WIDTH // 100:
            print('right')
            last_side = RIGHT
            keyboard.press('right')
            keyboard.release('left')
            keyboard.release('space')

    cv2.imshow("Camera", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        keyboard.release('space')
        keyboard.release('left')
        keyboard.release('right')
        break

camera.release()

cv2.destroyAllWindows()
