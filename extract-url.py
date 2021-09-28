# extract-url.py
# This program that will extract the URLs from an access.log file & store the URLs as strings in a list
# Author: Fatima Zeino

import re








ary = []


with open("access.log") as file:
 for line in file:
  url1 = re.findall('(https?://\S+)', line)
  #print(url1[0].replace('"',''))
  url=url1[0].replace('"','')
  if  url.__contains__('?'):
    page, query = url.split('?')
    names_values_dict = dict(pair.split('=') for pair in query.split('&'))
    names_values_list = [pair.split('=') for pair in query.split('&')]
    mydic = {}
    mydic['resource'] = page.replace('http://','')
    mydic['parameters'] = names_values_dict
    ary.append(mydic)

print(ary)




 


