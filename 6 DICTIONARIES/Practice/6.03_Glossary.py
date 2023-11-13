''' A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.
• Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.'''

# Create a glossary using a dictionary
glossary = {
    "variable": "A container for storing data in programming.",
    "function": "A block of code that performs a specific task and can be reused.",
    "loop": "A control structure that repeatedly executes a block of code.",
    "conditional statement": "A programming construct that allows different actions based on conditions.",
    "list": "An ordered collection of items that can store various data types."
}

# Print each word and its meaning
for word, meaning in glossary.items():
    print(word.capitalize() + ":")
    print(meaning)
    print()  # Print a blank line between each word-meaning pair

