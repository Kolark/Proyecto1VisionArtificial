import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


class Characteristics:
    """Clase para detectar características"""

    @staticmethod
    def find_face(frame):
        """
        Método para encontrar un rostro de una imagen

        :param frame: imagen en donde están los rostros
        :returns: posición en x, y, ancho y alto 
        """

        faces = face_cascade.detectMultiScale(frame, 1.3, 5)
        if len(faces) > 0:
            return *faces[0], True
        else:
            h, w = frame.shape
            return (w//2, h//2, 0, 0, False)
