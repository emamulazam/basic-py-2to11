''' Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city's dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it. '''

citys = {
    'dhaka': {
        'country': 'Bangladesh',
        'population': '2.6 Cr',
        'fact': "capital of Bangalsesh"
    },
    'tokio': {
        'county': 'Japan',
        'population': '6 Cr',
        'fact': "caital of Japan"
    },
    'dhili': {
        'country': 'India',
        'populatio': '1.5 Cr',
        'fact': "capital of India"
    }
}

for city, info in citys.items():
    print("Information of " + city.title() + "is-\n")
    for info_key, info_value in info.items():
            print(info_key.title() + " is " + info_value)
    print('')