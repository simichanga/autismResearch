import cv2 ### pip install opencv-python
## pip install opencv-contrib-python fullpackage
import matplotlib.pyplot as plt ## default plot library
from deepface import DeepFace ## pip install deepface

img = cv2.imread('image.jpg')

plt.imshow(img) ## by default BGR
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) ## converted to RGB

predictions = DeepFace.analyze(img)

print(predictions['dominant_emotion'])
