''' Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you'd like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once. '''

countries = ['bangladesh', 'uk', 'india', 'usa']

print(countries[0])
print(countries[0].title())
print(countries[-1])

countries[-1] = 'uae'
print(countries)

countries.append('usa')
print(countries)

countries.insert(0, "pakistan")
print(countries)

del countries[0]
print(countries)

poped_countries = countries.pop()
print(countries)
print(poped_countries)

countries.remove('uk')
print(countries)

countries.reverse()
print(countries)

countries.sort()
print(countries)
countries.sort(reverse=True)

print(len(countries))