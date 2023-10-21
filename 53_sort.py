# sort() method = used with lists
# sort() function = used with iterables

# list
students = ["Squidwards", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

students.sort()
# students.sort(reverse=True)

# for i in students:
#   print(i)


# tuple
students = ("Squidwards", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
sorted_students = sorted(students)
# sorted_students = sorted(students, reverse=True)

# for i in sorted_students:
#   print(i)


students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78)]

# students.sort() # by 

# grade = lambda grades:grades[1]
# students.sort(key=grade)
# # students.sort(key=grade, reverse=True)

age = lambda ages:ages[2]
students.sort(key=age)

# for i in students:
#   print(i)

students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr.Krabs", "C", 78))

sorted_students = sorted(students, key=age)

for i in sorted_students:
  print(i)
