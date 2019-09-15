#!/bin/python3
import json
import random

total = 0
model = []
with open('countries.txt', 'r') as file:
  for l in file:
    if len(l) >= 1 and len(l) <= 9 and random.randint(1,1) == 1:
      total = total + 1
      model.append(l.rstrip())
jsonString = json.dumps({ 'words' : model})
print(total)
with open('src/words.json','w') as file:
  file.write(jsonString)
