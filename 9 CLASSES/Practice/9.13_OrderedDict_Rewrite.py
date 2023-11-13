''' Start with Exercise 6-4 (page 108), where you
used a standard dictionary to represent a glossary. Rewrite the program using
the OrderedDict class and make sure the order of the output matches the order
in which key-value pairs were added to the dictionary.'''

from collections import OrderedDict

glossary = OrderedDict()

glossary ["variable"] = "A container for storing data in programming."
glossary ["function"] = "A block of code that performs a specific task and can be reused."
glossary ["loop"] = "A control structure that repeatedly executes a block of code."
glossary ["conditional statement"] = "A programming construct that allows different actions based on conditions."
glossary ["list"] = "An ordered collection of items that can store various data types."



for word, meaning in glossary.items():
    print(word.capitalize() + ":")
    print(meaning)
    print()