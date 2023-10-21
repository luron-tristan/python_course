# dictionary: a changeable, unordered collection of unique key:value pairs
# fast because they use hashin, allow us to access a value quicly
# => OBJECT in JS

capitals = {'USA': 'Washington DC',
            'India': 'New Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals['Germany']) # => error
# print(capitals.get('Germany'))  # => None
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('Russia')

for key, value in capitals.items():
    print(key, value)

capitals.clear()
print(capitals)
