# Print something in the terminal
print('hello')

# VARIABLES

# STRING
first_name = 'Tristan'
last_name = 'Luron'
full_name = first_name + " " + last_name

print("Hello " + full_name)
print(type(full_name))

# INT
age = 30
age += 1
print(age)
print(type(age))
print("Your age is: " + str(age))

# FLOAT
height = 250.5
print(height)
print(type(height))
print("Your height is: " + str(height) + 'cm')

# BOOLEAN
human = True
alien = False
print(human)
print(type(human))
print("Are you a human: " + str(human))

# MULTIPLE ASSIGNMENT
# name = "Triss"
# age = 30
# attractive = False

name, age, attractive = 'Triss', 30, True
print(name, age, attractive)

Spongebob = Patrick = Sandy = Squidward = 30
print(Spongebob)
