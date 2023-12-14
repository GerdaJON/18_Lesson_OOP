# 4th
#
# Create a Country class so that it contains population, area, country name. Also add the attribute is_big. Set it to True if at least 1 criteria is met:
#
# Population is greater than 20 million.
# Area is larger than 3 million square km.
# Also, create a method which compares a country's population density to another country object. Return a string in the following format:
#
# {country} has a {smaller / larger} population density than {other_country}
# Examples:
#
# australia = Country("Australia", 23545500, 7692024)
# andorra = Country("Andorra", 76098, 468)
#
# australia.is_big ➞ True
# andorra.is_big ➞ False
# andorra.compare_pd(australia) ➞ "Andorra has a larger population density than Australia"

# PAVYKO :)

class Country:
    def __init__(self, country, area, population):
        self.country = country
        self.area = area
        self.population = population

    def is_big(self):
        if self.population > 200000 or self.area > 3000000:
            return True
        else:
            return False

    def population_density(self):
        return self.population / self.area

    def get_country_name(self):
        return self.country

    def population_df(self):
        if first_country.population_density() > other_country.population_density():
            return f'{first_country.get_country_name()} has larger population density than {other_country.get_country_name()}'
        elif first_country.population_density() < other_country.population_density():
            return f'{first_country.get_country_name()} has smaller population than {other_country.get_country_name()}'
        else:
            return f'{first_country.get_country_name()} has equal population as {other_country.get_country_name()}'



first_country = Country("Australia", 23545500, 7692024)
other_country = Country("Andorra", 76098, 4680)

print(first_country.is_big())
print(other_country.is_big())
print(first_country.population_density())
print(other_country.population_density())
print(first_country.population_df())
print(other_country.population_df())