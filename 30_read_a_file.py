# with open closes automatically the file
try:
    with open('C:\\Users\\user\\projets\\python\\helloWorld\\30_test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print('This file was not found')

# print(file.closed)
