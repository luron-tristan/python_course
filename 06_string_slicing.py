# indexing[] or slice()
# [start:stop:step]
# start: inclusive, stop: exclusive, step: increment

name = "Triss Luron"

first_name = name[0: 4]
# first_name = name[:4] => start -> 4
last_name = name[6:8]
# last_name = name[6:] => 6 -> end
funky_name = name[0:10:2]
# funky_name = name[::2]
reversed_name = name[::-1]

print(first_name + ' ' + last_name)
print(funky_name)
print(reversed_name)

website1 = 'https://google.fr'
website2 = 'https://wikipedia.com'
slice = slice(len('https://'), -3)
print(website1[slice])
print(website2[slice])
