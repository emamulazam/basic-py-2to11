def city_countrys(city, country, population= ''):
    if population:
        city_country = city + ", " + country + " - population " + population
    else:
        city_country = city + ", " + country
    return city_country.title()