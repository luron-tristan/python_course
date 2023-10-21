#  exception = events detected during execution that interrupts the normal flow of a program

try:
    numerator = int(input('Enter a number to divide: '))
    denominator = int(input('Enter a number to divide by: '))
    result = numerator / denominator
except ZeroDivisionError as e:
    print(e)
    print("You can't divide by zero")
except ValueError as e:
    print(e)
    print("Enter numbers only")
except Exception as e:
    print(e)
    print("something went wrong...")
else:  # no exceptions
    print(result)
finally:  # whether or not we catch an exception
    print('This will always execute')
