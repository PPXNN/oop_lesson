import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

countries = []
with open(os.path.join(__location__, 'Countries.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        countries.append(dict(r))
#
# # Print the average temperature of all the cities
# print("The average temperature of all the cities:")
# temps = []
# for city in cities:
#     temps.append(float(city['temperature']))
# print(sum(temps)/len(temps))
# print()
#
# # Print all cities in Italy
# cities_temp = []
# my_country = 'Italy'
# for city in cities:
#     if city['country'] == my_country:
#         cities_temp.append(city['city'])
# print("All the cities in", my_country, ":")
# print(cities_temp)
# print()
#
# # Print the average temperature for all the cities in Italy
# temps = []
# my_country = 'Italy'
# for city in cities:
#     if city['country'] == my_country:
#         temps.append(float(city['temperature']))
# print("The average temperature of all the cities in", my_country, ":")
# print(sum(temps)/len(temps))
# print()
#
# # Print the max temperature for all the cities in Italy
# temps = []
# my_country = 'Italy'
# for city in cities:
#     if city['country'] == my_country:
#         temps.append(float(city['temperature']))
# print("The max temperature of all the cities in", my_country, ":")
# print(max(temps))
# print()
#
# # Print the min temperature for all the cities in Italy
# temps = []
# my_country = 'Italy'
# for city in cities:
#     if city['country'] == my_country:
#         temps.append(float(city['temperature']))
# print("The min temperature of all the cities in", my_country, ":")
# print(min(temps))
# print()


def filter(condition, dict_list):
    filtered_list = []
    for item in dict_list:
        if condition(item):
            filtered_list.append(item)
    return filtered_list


# Let's write a function to do aggregation given an aggregation function and an aggregation key
def aggregate(aggregation_key, aggregation_function, dict_list):
    _list = []
    for item in dict_list:
        value = float(item[aggregation_key])
        _list.append(value)

    return aggregation_function(_list)
# Let's write code to
# - print the average temperature for all the cities in Italy
cities_in_italy = filter(lambda x: x['country'] == 'Italy', cities)
avg_italy = aggregate("temperature", lambda x: sum(x)/len(x), cities_in_italy)
print(f"The average temperature of all the cities in Italy :\n{avg_italy}\n")
# - print the average temperature for all the cities in Sweden
cities_in_sweden = filter(lambda x:x["country"] == "Sweden", cities)
avg_sweden = aggregate("temperature", lambda x: sum(x)/len(x), cities_in_sweden)
print(f"The average temperature of all the cities in Sweden :\n{avg_sweden}\n")
# - print the min temperature for all the cities in Italy
min_italy = aggregate("temperature", lambda x: min(x),cities_in_italy)
print(f"The min temperature of all the cities in Italy :\n{min_italy}\n")
# - print the max temperature for all the cities in Sweden
max_sweden = aggregate("temperature", lambda x: max(x),cities_in_sweden)
print(f"The max temperature of all the cities in Sweden :\n{max_sweden}\n")
