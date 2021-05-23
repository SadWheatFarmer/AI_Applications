################################################################################
#Objective: Import an image from the Web
#API: None
# (previous API was IBM Watson Visual Recognition)
################################################################################


import cv2
print(cv2.__version__)

import urllib.request
from matplotlib import pyplot as plt
from pylab import rcParams


# Function to download an image and plot it.
def plt_image(image_url, size=(10, 8)):
    # Downloads an image from a URL, and displays it in the notebook
    urllib.request.urlretrieve(image_url,
                               "image.jpg")  # downloads file as "image.jpg"
    image = cv2.imread("image.jpg")

    # If image is in color, then correct color coding from BGR to RGB
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    rcParams['figure.figsize'] = size[0], size[1]  # set image display size

    plt.axis("off")
    plt.imshow(image, cmap="Greys_r")
    plt.show()


image_url = 'https://bostonglobe-prod.cdn.arcpublishing.com/resizer/BV6WbkWpxkhffO7rIqz2ukQXifQ=/1440x0/arc-anglerfish-arc2-prod-bostonglobe.s3.amazonaws.com/public/FKPJQWTKYEI6JAG535V2TRM35Y.jpg'
plt_image(image_url)