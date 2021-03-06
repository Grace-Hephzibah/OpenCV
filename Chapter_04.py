import cv2
import numpy as np

# For creating Black Image
img = np.zeros( (512, 512, 3), np.uint8)


# To color the whole image
img[:] = (255, 0, 0)

# To create line
cv2.line(img, (0,0), (300,300), (0,255,0), 3)

# To draw the rectangle
cv2.rectangle(img, (0,0), (250,350), (0,0,255), 2)

# To draw a circle
cv2.circle(img, (400,50), 30, (255, 255, 0), 5)

# Text on images
cv2.putText(img, "OPENCV", (300,100), cv2.FONT_ITALIC, 1, (0,150,0), 1)

cv2.imshow("Output Window", img)
cv2.waitKey(0)