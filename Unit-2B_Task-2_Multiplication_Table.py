n = int(input("Enter a number: "))

for i in range(1, 11):
    print(n, "x", i, "=", n*i)

    number = int(input("Enter a number: "))
i = 1  # start multiplier from 1

while i <= 10:
    product = number * i
    print(f"{number} x {i} = {product}")
    i += 1