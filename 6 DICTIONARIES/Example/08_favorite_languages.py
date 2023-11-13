favorite_languages = {
    'jen' : 'python',
    "sarsh" : "C",
    'edward' : 'ruby',
    'phil' : 'python'
}

print("The following languages have mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

# When you wrap set() around a list that contains duplicate items.