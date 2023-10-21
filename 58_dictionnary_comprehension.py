# dictionary comprehensions = create dictionaries using an expression
# can replace for loops and certain lambda functions

# 1. dictionary = {key: expression for (key, value) in iterable}
# 2. dictionary = {key: expression for (key, value) in iterable if conditional}
# 3. dictionary = {key: (if/else) for (key, value) in iterable}
# 4. dictionary = {key: function(value) for (key, value) in iterable}


cities_in_F = {"New York": 32, 'Boston': 75, "Los Angeles": 100, 'Chicago': 50}

# 1.
# cities_in_C = {key: round((value-32)*(5/9)) for (key, value) in cities_in_F.items()}
# print(cities_in_C)

# 2.
# weather = {"New York": "snowing", "Boston": "sunny", "Los Angeles": "sunny", "Chicago": 'cloudy'}
# sunny_weather = {key: value for (key, value) in weather.items() if value == "sunny"}

# print(sunny_weather)

# 3.
# desc_cities = {key: ("WARM" if value >= 40 else "COLD") for (key, value) in cities_in_F.items()}
# print(desc_cities)

# 4.
# def check_temp(value):
#   if value >= 70:
#     return "HOT"
#   elif 69 >= value >= 40:
#     return "WARM"
#   else:
#     return "COLD"

# more_desc_cities = {key: check_temp(value) for (key, value) in cities_in_F.items()}
# print(more_desc_cities)