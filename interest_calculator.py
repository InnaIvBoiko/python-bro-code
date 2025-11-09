principle = 0
rate = 0.0
time = 0

while principle <= 0:
    try:
        principle = float(input("Enter the principle amount (greater than 0): "))
        if principle <= 0:
            print("Please enter a valid amount greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while rate <= 0:
    try:
        rate = float(input("Enter the rate of interest (greater than 0): "))
        if rate <= 0:
            print("Please enter a valid rate greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

while time <= 0:
    try:
        time = int(input("Enter the time (in years, greater than 0): "))
        if time <= 0:
            print("Please enter a valid time greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")

interest = (principle * rate * time) / 100
print(f"The interest is: {interest}")

total = principle * pow((1 + rate / 100), time)
print(f"The total amount after {time} years is: ${total:,.2f}")