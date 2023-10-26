a = int(input("What's the first number?: "))
b = int(input("What's the second number?: "))
while b:
    a, b = b, a % b
print(a)
