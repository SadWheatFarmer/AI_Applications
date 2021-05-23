################################################################################
#Annoying note about installing OpenCV, numpy, beautifulSoup.
#1. Make sure the pip command is up to date.
#    Terminal:
#    'pathToPython.exe'*/Python38/python.exe -m pip install --upgrade pip
#    C:\Users\*\Local\Programs\Python\Python38\python.exe
#2. Install openCV and numpy packages
#    Terminal:
#    pip install opencv-python
#    pip install numpy
#3. Install package into pyCharm
#    File -> Settings -> Project:* -> Python Interpreter
#    Search for 'numpy', 'openCV-python', 'beautifulSoup
################################################################################


###
# All imports needed for AI Development.
import numpy
import pandas
import cv2
import requests
from bs4 import BeautifulSoup

print(numpy.__version__)
print(pandas.__version__)
print(cv2.__version__)
print(requests.__version__)
###