# Writing lines about Python to a file
with open("learning_python.txt", "w") as file:
    file.write("In Python you can define variables and assign values to them.\n")
    file.write("In Python you can create functions to organize your code.\n")
    file.write("In Python you can use libraries and modules to extend functionality.\n")

# Reading the file and printing its contents three times
# Method 1: Read the entire file
with open("learning_python.txt", "r") as file:
    content = file.read()
    print("Method 1 - Read entire file:")
    print(content)

# Method 2: Loop over the file object
with open("learning_python.txt", "r") as file:
    print("\nMethod 2 - Loop over the file:")
    for line in file:
        print(line, end="")

# Method 3: Store lines in a list and work with them outside the 'with' block
lines = []
with open("learning_python.txt", "r") as file:
    lines = file.readlines()

print("\nMethod 3 - Lines stored in a list:")
for line in lines:
    print(line, end="")
