#  index operator [] => gives access to a sequence's element (str, list, tuples...)

name = 'triss Luron!'

# if (name[0].islower()):
#     name = name.capitalize()

first_name = name[:5].upper()
last_name = name[6:].lower()
last_character = name[-1]

name = first_name + ' ' + last_name

print(name)
print(last_character)
