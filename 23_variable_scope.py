# scope = The region that a variable is recognized
# a variable is only available from inside the region it is created
# a global and locally scoped versions of a variable can be created

name = 'Bro'


def display_name():
    # name = 'Triss' # if removed, name = 'Bro
    print('inside the function', name)


display_name()
print('outside the function', name)

# variables order: LEGB
#  => Local, Enclosing, Global, Built-in
