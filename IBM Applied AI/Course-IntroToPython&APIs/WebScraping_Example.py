################################################################################
#Objective: Collect data from a wikipedia page and perform data analysis
#
#Uses 'BeautifulSoup' module to convert HTTP data to dataFrames
################################################################################

from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

#BeautifulSoup Example
html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, 'html5lib')
soup.prettify()
