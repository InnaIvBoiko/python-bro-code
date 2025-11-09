name = input("Enter your name: ")

# if name == "":
#     print("You did not enter a name.")
# else:
#     print(f"Hello, {name}!")

while name == "":
    print("You did not enter a name.")
    name = input("Enter your name: ")
    
print(f"Hello, {name}!")

age = int(input("Enter your age: "))    

while age <= 0:
    print("Age must be positive.")
    age = int(input("Enter your age: "))
    
print(f"You are {age} years old.")

food = input("Enter your favorite food (q to quit): ")

while not food == "q":
    print(f"Your favorite food is {food}.")
    food = input("Enter your favorite food (q to quit): ")

print("Goodbye!")

num = int(input("Enter a positive number (0 to 10): "))

while num < 0 or num > 10:
    print("Number must be between 0 and 10.")
    num = int(input("Enter a positive number (0 to 10): "))
    
print(f"You entered {num}.")