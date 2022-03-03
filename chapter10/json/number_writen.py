import json

numbers = [2,3,5,7,11,13]

file_name = 'number.json'
with open(file_name, 'w') as f_obj:
    json.dump(numbers,f_obj) #<< dump saves the data to our file