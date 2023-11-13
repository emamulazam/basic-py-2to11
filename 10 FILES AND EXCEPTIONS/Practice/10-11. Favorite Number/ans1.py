import json

f_num = input("Enter your favorite number: ")
filename = 'f_num.json'
with open(filename, 'w') as f_obj:
    json.dump(f_num, f_obj)