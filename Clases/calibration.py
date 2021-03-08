import cv2
import numpy as np


class Calibration:

    @staticmethod
    def calibrate(ROI):
        hsv = cv2.cvtColor(ROI, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        HueMean = h.mean()
        SatMean = s.mean()
        ValMean = v.mean()
        HueSTD = np.std(h)
        SatSTD = np.std(s)
        ValSTD = np.std(v)

        HueMIN = (HueMean-HueSTD*3) % 180
        SatMIN = np.clip(SatMean-SatSTD*5, 0, 255)
        ValMIN = np.clip(ValMean-ValSTD*5, 0, 255)
        HueMAX = (HueMean+HueSTD*3) % 180
        SatMAX = np.clip(SatMean+SatSTD*5, 0, 255)
        ValMAX = np.clip(ValMean+ValSTD*5, 0, 255)

        return np.array((HueMIN, SatMIN, ValMIN)), np.array((HueMAX, SatMAX, ValMAX))
