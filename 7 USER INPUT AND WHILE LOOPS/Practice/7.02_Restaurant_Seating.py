''' Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they'll have to wait for a table. Otherwise, report that their table is ready. '''

question = "How many people are in their dinner group? "
number = int(input(question))

if number <= 8:
    print("Their table is ready.")
else:
    print("They'll have to wait for a table.")