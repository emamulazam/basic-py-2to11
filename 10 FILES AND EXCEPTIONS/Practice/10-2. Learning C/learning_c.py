file = "learning_python.txt"

with open(file, 'r') as file_object:

    for line in file_object:
        modifi = line.replace('Python', 'C')

        print(modifi.rstrip())