import sys
import re

f = open("romeo_juliet.txt",'r+')
file_text = f.read()
match = re.findall(r'\(([\w\s]+)\[(\d+)\]\)', file_text)
print('Please select words matching the follow parts of speach')
selections = []
for element in match:
  selection=input('({})  {}.'.format(element[0],element[1]))
  selections.append([element[0],element[1],selection ])
for element in selections:
  file_text = re.sub(r'\({}\[{}\]\)'.format(*element),element[2], file_text)
print(file_text)
