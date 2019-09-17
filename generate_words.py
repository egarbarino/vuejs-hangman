#!/usr/bin/python3
# This script generates a list of  words of up to 9 letters that
# is saved as a Json array at src/words.json

import json
import random

total = 0
model = []
with open('words_countries.txt', 'r') as file:
  for l in file:
    if len(l) >= 1 and len(l) <= 9 and random.randint(1,1) == 1:
      total = total + 1
      model.append(l.rstrip())
jsonString = json.dumps({ 'words' : model})
print(total)
with open('src/words.json','w') as file:
  file.write(jsonString)
