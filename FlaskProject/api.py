# Importing some libraries
import cv2
from sklearn.cluster import KMeans
import numpy as np
import cv2
from collections import Counter
from skimage.color import rgb2lab, deltaE_cie76
import os
import requests
from skimage import io
# Importing all the important libraries

# Function for getting the HEX color from the RGB color.
def RGB2HEX(color):
    return "#{:02x}{:02x}{:02x}".format(int(color[0]), int(color[1]), int(color[2]))

# Function for getting the colors of our given input
def get_colors(src):
    
    # Reading the image from the source URL
    image = io.imread(src)
    modified_image = cv2.resize(image, (600, 400), interpolation = cv2.INTER_AREA)
    modified_image = modified_image.reshape(modified_image.shape[0]*modified_image.shape[1], image.shape[2])
    
    # Picking up the top 2 colors and then predicting it 
    clf = KMeans(n_clusters = 2)
    labels = clf.fit_predict(modified_image)
    
    counts = Counter(labels)
    
    counts = dict(sorted(counts.items(),key=lambda item: item[1],reverse=True))

    center_colors = clf.cluster_centers_

    # Getting all the colors in the form of dictionary in the hex_colors dictionary
    hex_colors = {}

    hex_colors['dominant_color'] = RGB2HEX(center_colors[0])
    hex_colors['logo_color'] = RGB2HEX(center_colors[1])

    return hex_colors
