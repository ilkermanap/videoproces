import cv2
import numpy as np

class Picture:
    def __init__(self, data):
        self.image = data

    @classmethod
    def fromfilename(cls, filename):
        return cls(cv2.imread(filename))

    @classmethod
    def fromarray(cls, data):
        return cls(data)

    def check_skin(self):
        lower = np.array([0,48,80], dtype="uint8")
        upper = np.array([20,255,255], dtype="uint8")
        
        converted = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        skinmask = cv2.inRange(converted, lower, upper)
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11,11))
        skinmask = cv2.erode(skinmask, kernel, iterations = 2)
        skinmask = cv2.dilate(skinmask, kernel, iterations = 2)
        skinmask = cv2.GaussianBlur(skinmask, (3,3),0)
        skin = cv2.bitwise_and(self.image, self.image, mask=skinmask)
        gray_image = cv2.cvtColor(skin, cv2.COLOR_BGR2GRAY)

        nonzero = cv2.countNonZero(gray_image)
        return nonzero, skin

    
