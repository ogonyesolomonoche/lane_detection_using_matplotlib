import matplotlib.pylab as plt
import cv2
import numpy as np

image = cv2.imread("road.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

print(image.shape)
height = image.shape[0]
width = image.shape[1]

plt.imshow(image)
plt.show()
