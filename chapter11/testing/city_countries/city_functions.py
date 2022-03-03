

def get_formatted_cities(city_name,country_name,population=0):
    full_city = city_name + ', ' + country_name 
    if population:
        if population:
            full_city += ' - population ' + str(population)
    return full_city.title()

