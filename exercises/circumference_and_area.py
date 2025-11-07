import math

radius = float(input("Enter the radius of the circle: "))

circumference = 2 * math.pi * radius

print(f"The circumference of the circle with radius {radius} is {round(circumference, 2)} cm.")

# area = math.pi * radius ** 2
area = math.pi * pow(radius, 2)
print(f"The area of the circle with radius {radius} is {round(area, 2)} cm².")