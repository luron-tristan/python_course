age = int(input('how old are you? '))

if age == 100:
    print('congrats you century old')
elif age >= 18:
    print('ok you are an adult')
elif age < 0:
    print("you haven't been born yet")
else:
    print('go away kid')
