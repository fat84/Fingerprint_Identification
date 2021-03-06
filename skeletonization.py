import cv2
import numpy as np


def execute(file_path):
    img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)

    img = cv2.medianBlur(img, 5)

    ret, img = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while not done:
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True
    return skel
