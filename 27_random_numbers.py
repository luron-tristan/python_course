import random

x = random.randint(1, 6)
y = random.random()

my_list = ['rock', 'paper', 'scissors']
z = random.choice(my_list)

print(x)
print(y)
print(z)

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
random.shuffle(cards)
print(cards)
