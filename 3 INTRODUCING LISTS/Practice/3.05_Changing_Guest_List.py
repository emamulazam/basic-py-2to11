''' You just heard that one of your guests can't make the
dinner, so you need to send out a new set of invitations. You'll have to think of
someone else to invite.
• Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can't make it.
• Modify your list, replacing the name of the guest who can't make it with
the name of the new person you are inviting.
• Print a second set of invitation messages, one for each person who is still
in your list. '''

names = ['ali', 'niloy', 'farhan']

message = names[2].title() + ", can't make the dinner."
print(message)

names[2] = "riya"

message = names[0].title() + ", you are invited to the dinner."
print(message)

message = names[1].title() + ", you are invited to the dinner."
print(message)

message = names[2].title() + ", you are invited to the dinner."
print(message)

