# extract-url.py
# This program that will extract the URLs from an access.log file & store the URLs as strings in a list
# Author: Fatima Zeino

import re
urlsFinal=[]

with open("access.log") as file:
 for line in file:
  url = re.findall('(https?://\S+)', line)
  urlsFinal.append(url)
  # print(url)
print(urlsFinal)