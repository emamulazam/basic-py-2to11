''' Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician's name. Call show_magicians() to
see that the list has actually been modified. '''

def make_great(new_magicians, magician_names):
    for new_magician in new_magicians:
        magician_names.append(new_magician)

magician_names = ['ali', 'niloy', 'anis']
new_magicians = ['rony', 'rayhan', 'nila']

make_great(new_magicians, magician_names)
print(magician_names)
