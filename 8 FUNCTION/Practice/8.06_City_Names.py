''' Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that's returned. '''

def city_country(city_name, country_name):
    city_country_name = city_name.title() + ", " + country_name.title()
    return city_country_name

cc = city_country('barishal', 'bangladesh')
print(cc)
