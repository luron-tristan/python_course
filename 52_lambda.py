# lambda function = function wriiten in 1 line using lambda keyword
# accepts any number of argument, but only has onr rcptrddion
# think of it as a shortcut
# useful if needed for a short period of time, throw-away

# lambda parameters:expression

# def double(x):
#   return x * 2
# print(double(5))

double = lambda x:x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z
full_name = lambda first_name, last_name: first_name + " " + last_name
age_check = lambda age: True if age >= 18 else False

print(double(5))
print(multiply(5, 6))
print(add(5, 6, 7))
print(full_name("Tristan", "Luron"))
print(age_check(13))
print(age_check(19))