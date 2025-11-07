import math

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

# c = math.sqrt(a**2 + b**2)
c= math.sqrt(math.pow(a, 2) + math.pow(b, 2))

print(f"The length of the hypotenuse c is: {c}")