# OpenCV-Python
 I am learning OpenCV in Python

# Topics
- Introduction to Images
- Installations 
- Chapter 01: Read Images, Videos and Webcams
- Chapter 02: Basic Functions
- Chapter 03: Resize and Crop
- Chapter 04: Shapes and Text 
- Chapter 05: Warp Perspective
- Chapter 06: Joining Images
- Chapter 07: Colour Detection
- Chapter 08: Contour / Shape Detection
- Chapter 09: Face Detection

# Projects 
- Project 1 :
<a href = "https://github.com/Grace-Hephzibah/Virtual-Paint"> 
Virtual Paint </a>
  
# Introduction to Images
Consider a 2d-box of dimension (10 x 10). Draw equal 
lines such that each interior square is (1 x 1). Now 
there are 100 such small squares in the 2d-box.
<br><br>
Every shaded region (black) is denoted by a value 0. And 
every non-shaded region (white) is denoted by a value 1.
In technical terms, each sqaure is a pixel.
## Types of Images
- VGA ->  640 x  480
- HD  -> 1280 x  720
- FHD -> 1920 x 1080
- 4K  -> 3840 x 2160
## Black and White Images
Generally 2^8 = 256 bit resolution is used.
- 0 is black 
- 255 is white 
- The rest are shades of gray

Those images are called 8 bits or 256 levels.
## Coloured Images
Coloured images have 3 channels. They are RGB. 
- RGB stands for Red Green Blue
In OpenCV Convention, BGR term is used instead of RGB.

# Installations 
- Install Python 3.7.6 -> It works well with OPENCV
- Install PyCharm -> A free comfortable IDE

## Packages to install
- opencv-python --> This is the OPENCV Package 
- numpy --> Used in arrays to analyse the images

## Imported as 
- import cv2
- import numpy as np