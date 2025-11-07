age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult.")
elif age == 18:
    print("You have just become an adult.")
elif age > 13:
    print("You are a teenager.")
elif age == 13:
    print("You have just become a teenager.")
elif age < 0:
    print("You haven't been born yet.")
else:
    print("You are a child.")    