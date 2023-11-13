favorite_languages = {
    'jen' : ['python', 'ruby'],
    "sarsh" : ["c",],
    'edward' : ['ruby', 'go'],
    'phil' : ['python','haskell']
}

for name, languages in favorite_languages.items(): # taking keys and values
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())