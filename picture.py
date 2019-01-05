import cv2
import numpy as np
import face_recognition as fr

class Picture:
    def __init__(self, data):
        if type(data) is str:
            self.image = cv2.imread(data)
        else:
            self.image = data
        self.faces = {}
        self.rgb = self.image[:, :, ::-1]
        self.face_encodings = []

    @classmethod
    def fromfilename(cls, filename):
        return cls(cv2.imread(filename))

    @classmethod
    def fromarray(cls, data):
        return cls(data)

    def save(self, name):
        cv2.imwrite(name, self.image)
    
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

    
    def find_faces(self):
        facelocations = fr.face_locations(self.rgb)

        for id, face in enumerate(facelocations):
            top, right, bottom, left = face
            fc = fr.face_encodings(self.rgb[top:bottom, left:right])
            if len(fc) > 0:
                face_enc = fc[0]
                self.face_encodings.append(face_enc)
                self.faces[id] = Face(self.rgb[top:bottom, left:right], face_enc)


class Face(Picture):
    def __init__(self,data, face_encoding=None):
        Picture.__init__(self, data)
        if face_encoding is not None:
            self.face_encoding = face_encoding
        else:
            self.face_encoding = fr.face_encodings(self.rgb)[0]

    
    def face_match(self, picture, tolerance = 0.50):
        return fr.compare_faces(picture.face_encodings, self.face_encoding, tolerance = tolerance)
        
