################################################################################
#Objective: Download an image, compress image sizes by K Means Clustering.
#
#K Means Clustering
#   Idea: Plotting each data point and then dividing the set into an 'n'
#           number of unique groups. As 'n' decreases, so does image size.
################################################################################

# importing OpenCV and urllib for downloading and displaying the bunny image
import urllib.request
import cv2

# loading standard python modules
import os
import math
import matplotlib.pyplot as plt

# We are using the sklearn python module and are importing the in built KMeans
# function from it
from sklearn.cluster import KMeans

# we import numpy here to transform image dimensions
import numpy as np

# Download bunny image
bunny_image_url = "http://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/CV0101/Dataset/bunny.png"
urllib.request.urlretrieve(bunny_image_url, "bunny.png") # downloads file as "bunny.png"
im = cv2.imread("bunny.png")

# We read a bunny image here and display it
img_corrected = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(img_corrected)
plt.show()
print("Original size of bunny's image is: {} Kilo Bytes".format(str(math.ceil((os.stat('bunny.png').st_size)/1000))))

# Show example of K Means Clustering
k_means_url = "http://i.stack.imgur.com/cIDB3.png"
urllib.request.urlretrieve(k_means_url, "K_Means_clustering.png") # downloads file as "K_Means_clustering.png"
k_means_im = cv2.imread("K_Means_clustering.png")
k_means_im_corrected = cv2.cvtColor(k_means_im, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(k_means_im_corrected)
plt.show()

# Extracting num_rows and num_cols from bunny's image (stored in im variable)
num_rows = im.shape[0]
num_cols = im.shape[1]
transform_image_for_KMeans = im.reshape(num_rows * num_cols, 3)

# Perform KMeans to compress image, here K = 8 clusters
n_clusters = 8
kmeans = KMeans(n_clusters)
kmeans.fit(transform_image_for_KMeans)

cluster_centroids = np.asarray(kmeans.cluster_centers_,dtype=np.uint8)

# labels represent the label of each pixel and which cluster it belongs to
labels = np.asarray(kmeans.labels_,dtype=np.uint8 )
labels = labels.reshape(num_rows,num_cols);

compressed_image = np.ones((num_rows, num_cols, 3), dtype=np.uint8)
for r in range(num_rows):
    for c in range(num_cols):
        compressed_image[r, c, :] = cluster_centroids[labels[r, c], :]

cv2.imwrite("compressed_bunny.png", compressed_image)
compressed_bunny_im = cv2.imread("compressed_bunny.png")
compressed_bunny_im_corrected = cv2.cvtColor(compressed_bunny_im, cv2.COLOR_BGR2RGB)
plt.axis('off')
plt.imshow(compressed_bunny_im_corrected)

print("Compressed size of bunny's image is: {} Kilo Bytes".format(str(math.ceil((os.stat('compressed_bunny.png').st_size)/1000))))