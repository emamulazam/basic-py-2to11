filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")


''' read mode ('r'), write mode ('w'), append mode ('a'), or a mode that allows
you to read and write to the file ('r+'). If you omit the mode argument,
Python opens the file in read-only mode by default.'''