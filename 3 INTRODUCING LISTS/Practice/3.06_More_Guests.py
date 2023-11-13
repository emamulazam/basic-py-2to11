''' You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
• Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
• Use insert() to add one new guest to the beginning of your list.
• Use insert() to add one new guest to the middle of your list.
• Use append() to add one new guest to the end of your list.
• Print a new set of invitation messages, one for each person in your list. '''


names = ['ali', 'niloy', 'farhan']

names.insert(0, "riya")
names.insert(2, "ronry")
names.insert(5, "helal")


message = names[0].title() + ", you are invited to the dinner."
print(message)

message = names[1].title() + ", you are invited to the dinner."
print(message)

message = names[2].title() + ", you are invited to the dinner."
print(message)

message = names[3].title() + ", you are invited to the dinner."
print(message)

message = names[4].title() + ", you are invited to the dinner."
print(message)

message = names[5].title() + ", you are invited to the dinner."
print(message)