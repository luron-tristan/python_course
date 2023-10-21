# str.format() = optional method that gives users
# more control when displaying output

# animal = 'cow'
# item = 'moon'

# print('The', animal, 'jumped over the', item)
# print("The {} jumped over the {}".format(animal, item))
# print("The {0}{1} jumped over the {0}".format(
#     item, animal))  # positional argument
# print("The {astra}{beast} jumped over the {astra}".format(
#     beast="cow", astra='moon'))  # keyword argument
# text = "The {} jumped over the {}"
# print(text.format(animal, item))

# name = 'Triss'
# print('Hello, my name is {}'.format(name))
# print('Hello, my name is {some_name:10}. Nice to meet you'.format(
#     some_name=name))
# print('Hello, my name is {:10}. Nice to meet you'.format(name))
# print('Hello, my name is {:<10}. Nice to meet you'.format(name))
# print('Hello, my name is {:>10}. Nice to meet you'.format(name))
# print('Hello, my name is {:^10}. Nice to meet you'.format(name))

number = 3.14159
number2 = 1000

print('The number pi is {:.3f}'.format(number))
print('the number is {:,}'.format(number2))
print('the number is {:b}'.format(number2))  # binary
print('the number is {:o}'.format(number2))  # octo
print('the number is {:x}'.format(number2))  # hexa
print('the number is {:e}'.format(number2))  # scientific
print('the number is {:E}'.format(number2))  # SCIENTIFIC
