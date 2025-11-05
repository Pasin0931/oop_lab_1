import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter(condition, dict_):
    temp = []
    for i in dict_:
        if condition(i):
            temp.append(i)
    return temp
    
def aggregate(key_, func_, dict_):
    temp = [float(i[key_]) for i in dict_ if i[key_]]
    return func_(temp)
        

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()

# Print all cities in Germany
print("Cities in Germany")
filtered_list = filter(lambda x: x["country"] == "Germany", cities)
for city in filtered_list:
    print(city["city"])
print()

# Print all cities in Spain with a temperature above 12°C
print("Cities in Spain with a temperature above 12°C")
filtered_list = filter(lambda x: x["country"] == "Spain" and float(x["temperature"]) > 12, cities)
for city in filtered_list:
    print(city["city"])
print()

# Count the number of unique countries
print("Unique countries")
unique_countries = set([city["country"] for city in cities])
print(len(unique_countries))
print()

# Print the average temperature for all the cities in Germany
print("Average temperature for all the cities in Germany")
germany_cities = filter(lambda x: x["country"] == "Germany", cities)
avg_temp = aggregate("temperature", lambda t: sum(t)/len(t), germany_cities)
print(avg_temp)
print()

# Print the max temperature for all the cities in Italy
print("Max temperature for all the cities in Italy")
italy_cities = filter(lambda x: x["country"] == "Italy", cities)
max_temp = aggregate("temperature", max, italy_cities)
print(max_temp)
print()