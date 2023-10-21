# tuple: collections which are ordered and unchangeable
# used to group together related data

student = ('Triss', 30, "male")

print(student.count('Triss'))
print(student.index('male'))

for x in student:
    print(x)

if "Triss" in student:
    print('Triss is here')
