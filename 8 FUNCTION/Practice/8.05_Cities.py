''' Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country. '''

def desceibe_city(city_name, country_name= "Bangladesh"):
    print(city_name.title() + " is in " + country_name.title() + '.')

desceibe_city(city_name= "barishal")
desceibe_city(city_name= "tokio", country_name= "japan")