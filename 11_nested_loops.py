rows = int(input("How many rows?: "))
columns = int(input("How many colmuns?: "))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()
