# *args = parameter that will pack all arguments into a tuple
# useful so that a function can accept a varying amount of arguments

# def add(num1, num2):
#   sum = num1 + num2
#   return sum

# print(2, 6, 8) # not working because only 2 args in add()

def add(*nums):
    sum = 0
    # nums[0] = 0 # tuple => ordered and unchangeable
    nums = list(nums)
    nums[0] = 0
    for i in nums:
        sum += i
    return sum


print(add(1, 2, 3, 4, 5, 6))
