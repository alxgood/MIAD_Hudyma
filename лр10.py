import cv2
from matplotlib import pyplot as plt
import numpy as np
from os import listdir
from os.path import isfile, join
def find_object(_image_path,_xml_path):
    classifier = cv2.CascadeClassifier(_xml_path)
    pixels = cv2.imread(_image_path)
    values = classifier.detectMultiScale3(
        pixels,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags = cv2.
        CASCADE_SCALE_IMAGE,
        outputRejectLevels = True
        )
    boxes = values[0]
    scores = list(values[2])
    scores.append(0)
    drow_rect(values[0],pixels)
    plt.imshow(pixels)
    plt.show()
    print("Recognition score is: "+str(scores[0]))
def drow_rect(_boxes,_pixels):
    for box in _boxes:
        x, y, width, height = box
        x2, y2 = x + width, y + height
        cv2.rectangle(_pixels, (x, y), (x2, y2), (0, 0, 255), 5)
xml_path = 'haarcascade_frontalface_default.xml'
images_path = 'photos'
images = [f for f in listdir(images_path) if isfile(join(images_path, f))]
for image in images:
    find_object(images_path+'/'+image,xml_path)

xml_path = 'haarcascade_russian_plate_number.xml'
image_path = 'car.jpg'
find_object(image_path,xml_path)