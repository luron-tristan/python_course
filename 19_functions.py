def hello(first_name, age, last_name=""):
    print('hello ' + first_name + " " + last_name, end=", ")
    print('have a nice day, you ' + str(age) + ' yo person')
    # print('have a nice day, you', age, 'person')


hello('James', 54)
hello('Maria', 19)
my_name = "Triss"
hello(my_name, 30, "Luron")
