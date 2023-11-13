import json

f_name = "f_num.json"
with open(f_name) as f_obj:
    num = json.load(f_obj)

print(f"I know your favorite number! It's {num}" )