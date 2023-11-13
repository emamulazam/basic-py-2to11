''' Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians' names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician's name. '''

def make_great(magician_names, new_list):
    for magician_name in magician_names:
        great = "Great Magician " + magician_name.title() 
        new_list.append(great)
    return new_list

new_list = []
magician_names = ['ali', 'niloy', 'anis']
make_great(magician_names, new_list)
print(new_list)
