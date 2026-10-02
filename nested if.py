a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b:
    if a > c:
        print("A is largest")
    else:
        print("C is largest")
else:
    if b > c:
        print("B is largest")
    else:
        print("C is largest")