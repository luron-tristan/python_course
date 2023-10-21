#  keyword arguments = arguments preceded by an identifier when we pass them to a function
# the order of the arguments doesn't matter, unlike positional argument
# Python knows the names of the arguments that our function receives

def hello(first, middle, last):
    print(first + " " + middle + " " + last)


hello(last="Luron", first="Hello", middle="Tristan")
