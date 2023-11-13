''' Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed. '''



usernames = ['admin']

if usernames:
    print("Not emtpy users")
else:
    print('We need to find some users!')

usernames.clear()

if usernames:
    print("hi")
else:
    print('We need to find some users!')