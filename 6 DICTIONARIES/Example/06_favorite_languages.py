favorite_languages = {
    'jen' : 'python',
    "sarsh" : "C",
    'edward' : 'ruby',
    'phil' : 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")
    
# for name in favorite_languages.keys(): # print keys
#     print(name.title())
# for name in favorite_languages.values(): # print values
#     print(name.title())