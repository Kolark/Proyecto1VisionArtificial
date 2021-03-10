import cv2
import numpy as np
import keyboard

from clases.tools import Characteristics
from clases.keyboard_controller import KeyboardController


LEFT = 0
RIGHT = 1

WIDTH = HEIGHT = 0

LEFT_PORCENT = 30
RIGHT_PORCENT = 30
BOTTON_PORCENT = 30


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
             (LEFT_PORCENT * WIDTH // 100, HEIGHT), (0, 255, 0), 3)
    # Límite derecho
    cv2.line(frame, (WIDTH - RIGHT_PORCENT *
                     WIDTH // 100, 0), (WIDTH - RIGHT_PORCENT *
                                        WIDTH // 100, HEIGHT), (0, 255, 0), 3)
    # Límite inferior
    cv2.line(frame, (0, HEIGHT - BOTTON_PORCENT * HEIGHT // 100),
             (WIDTH, HEIGHT - BOTTON_PORCENT * HEIGHT // 100), (0, 255, 0), 3)

    # Convertirlo a escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    x, y, w, h = Characteristics.find_face(gray)

    # Recuadro de la cara
    cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 255, 255), 2)

    center = ((x + w)//2, (y + h)//2)

    # # Si tiene el rostro en el centro
    # if center[0] > LEFT_PORCENT * WIDTH // 100 and \
    #         center[0] < WIDTH - RIGHT_PORCENT * WIDTH // 100 and \
    #         center[1] > HEIGHT - BOTTON_PORCENT * HEIGHT // 100:

    #     if keyboard.is_pressed('left'):
    #         keyboard.release('left')
    #     if keyboard.is_pressed('right'):
    #         keyboard.release('right')
    #     if keyboard.is_pressed('space'):
    #         keyboard.release('space')

    # # Si tiene el rostro en la parte izquierda
    # elif center[0] < LEFT_PORCENT * WIDTH // 100:

    #     last_side = LEFT
    #     keyboard.press('left')
    #     keyboard.release('space')

    # # Si tiene el rostro en la parte derecha
    # elif center[0] > WIDTH - RIGHT_PORCENT * WIDTH // 100:

    #     last_side = RIGHT
    #     keyboard.press('right')
    #     keyboard.release('space')

    # # Si tiene el rostro en la parte inferior
    # elif center[1] < HEIGHT - BOTTON_PORCENT * HEIGHT // 100:

    #     if last_side == LEFT:
    #         keyboard.press('left')
    #     elif last_side == RIGHT:
    #         keyboard.press('right')

    #     keyboard.press('space')

    cv2.imshow("Captura", gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        keyboard.release('space')
        keyboard.release('left')
        keyboard.release('right')
        break

camera.release()

cv2.destroyAllWindows()
