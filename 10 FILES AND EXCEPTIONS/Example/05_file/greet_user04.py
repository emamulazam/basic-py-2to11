import json

filenam = 'username.json'

with open(filenam) as f_obj:
    username = json.load(f_obj)
    print("Wellcom back, " + username + "!")