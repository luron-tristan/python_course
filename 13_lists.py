# lists = used to store multiple items in a single variable
# => ARRAY in JS

food = "pizza"
print(food)

food = ["pizza", 'burger', 'nutella', 'broccoli']

food[2] = 'salad'

print('choose your menu', food)
print("I'll have a", food[3])


# food.append("carrot cake")
# food.remove('burger')
# food.pop()
# food.insert(1, 'chips')
# food.sort()
# food.clear()

for x in food:
    print(x)
