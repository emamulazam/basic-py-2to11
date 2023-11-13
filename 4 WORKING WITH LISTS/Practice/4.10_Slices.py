''' Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program's list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list. '''

one_million = [value for value in range(1,1000001)]

first_three_items = one_million[:3]
middle_three_items = one_million[498:501]
last_three_items = one_million[-3:]

print(first_three_items)
print(middle_three_items)
print(last_three_items)