''' Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll. '''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

list = ['roney',"riya" , 'roy']

for a in favorite_languages.keys():
    list.append(a)

for b in list:
    if b in favorite_languages.keys():
        print(b.title() + ', thanking them for responding')
    else:
        print(b.title() + ', take the poll')