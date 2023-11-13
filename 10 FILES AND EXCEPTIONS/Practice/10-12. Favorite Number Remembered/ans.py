import json
filename = 'f_num.json'
try:
    with open(filename) as f_obj:
        num = json.load(f_obj)
    print(f"I know your favorite number! It's {num}" )

except FileNotFoundError:
    f_num = input("Enter your favorite number: ")
    with open(filename, 'w') as f_obj:
        json.dump(f_num, f_obj)

    


