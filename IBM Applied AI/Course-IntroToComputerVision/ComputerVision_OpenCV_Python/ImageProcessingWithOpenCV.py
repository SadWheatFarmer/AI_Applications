################################################################################
#Objective: Process a downloaded image using Canny Edge Detection and pixel
#               intensity histograms.
#Procedure
# 1) Download image
# 2) Convert image from BGR -> RGB
# 3) Remove axis from around image
# 4) Change size of image
#
#Techniques
# 1) Canny Edges - https://docs.opencv.org/master/da/d22/tutorial_py_canny.html?utm_email=Email&utm_source=Nurture&utm_content=000026UJ&utm_term=10006555&utm_campaign=PLACEHOLDER&utm_id=SkillsNetwork-Courses-IBMDeveloperSkillsNetwork-CV0101EN-SkillsNetwork-19816089
# 2) Historgram - Grayscale
# 3) Historgram - RGB
################################################################################

import cv2

#Download, check and plot image
import urllib.request
import os
from matplotlib import pyplot as plt

#Edit image size
from pylab import rcParams


# Download an image of your choosing and display it
mj_url = "https://i.ebayimg.com/images/g/AA8AAOSwLN5WkIx8/s-l400.jpg"
mj_filename = "mj_jump.jpg"
urllib.request.urlretrieve(mj_url, mj_filename) # downloads file as "mj_jump.jpg"

#   check: Is file in directory?
inFile = mj_filename in os.listdir(os.curdir)
mj = cv2.imread(mj_filename)
if(inFile):
    print("Is file {} inside the executing directory? Answ: {}".format(
        mj_filename, inFile))

    # [DEBUG] Show initial BGR image.
    plt.title('Jumping MJ - BGR')
    plt.imshow(mj)
    plt.show()

    # Show convert BGR image to RGB.
    plt.title('Jumping MJ - RGB')
    mj_corrected = cv2.cvtColor(mj, cv2.COLOR_BGR2RGB)
    plt.imshow(mj_corrected)
    plt.show()

    # Remove axis around image
    plt.axis("off")

    # Change image size & Convert image to Grayscale
    gray_mj = cv2.cvtColor(mj, cv2.COLOR_BGR2GRAY)
    rcParams['figure.figsize'] = 8, 4
    plt.title('Jumping MJ - Grayscale')
    plt.imshow(gray_mj, cmap='gray')
    plt.show()

    #######################################
    # Image Analysis Techniques.
    #######################################
    # See Canny Edge Detection (see file header for Canny documentation link)
    thresholds = [100, 200]
    edges = cv2.Canny(mj_corrected,
                      thresholds[0],
                      thresholds[1])
    rcParams['figure.figsize'] = 8, 4
    plt.title('Jumping MJ - Canny[{}, {}]'.format(thresholds[0], thresholds[1]))
    plt.imshow(edges, cmap = 'gray')
    plt.show()

    # Histograms - Grayscale
    rcParams['figure.figsize'] = 8, 4
    plt.hist(gray_mj.ravel(), 256, [0, 256])
    plt.title('Histogram of Grayscale {}'.format(mj_filename))
    plt.axis("on")
    plt.show()

    # Histograms - RGB
    rcParams['figure.figsize'] = 8, 4
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([mj], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.axis("on")
    plt.title('Histogram of RGB {}'.format(mj_filename))
    plt.show()

else:
    print("File not in directory")