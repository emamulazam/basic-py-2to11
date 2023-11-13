favorite_languages = {
    'jen' : 'python',
    "sarsh" : "C",
    'edward' : 'ruby',
    'phil' : 'python'
}

friends = ['phil', 'sarsh']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print("  Hi " + name.title() +
              ", I see your favorite language is " +
              favorite_languages[name].title() + "!")
        
# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!")

# for name in sorted(favorite_languages.keys()):
#     print(name.title() + ", thank you for taking the poll.")

'''This for statement is like other for statements except that we've wrapped
the sorted() function around the dictionary.keys() method. This tells Python
to list all keys in the dictionary and sort that list before looping through it.
The output shows everyone who took the poll with the names displayed in
order: '''