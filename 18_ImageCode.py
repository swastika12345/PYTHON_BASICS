#Image code
import numpy as np
import cv2
from sklearn.mixture import GaussianMixture as GMM
from google.colab import files
uploaded=files.upload()

#Print image
from google.colab.patches import cv2_imshow
import cv2
img = cv2.imread('image (2).png', cv2.IMREAD_UNCHANGED)
cv2_imshow(img)