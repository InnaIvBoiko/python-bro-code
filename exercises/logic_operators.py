temp = 25
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("Extreme temperature!")
    print("Stay indoors!")
else:
    print("Normal weather.")
    print("Enjoy your day outside!")
    
if temp >= 28 and not is_raining:
    print("It's HOT outside!")
    print("It's Sunny!")
elif temp <= 0 and not is_raining:
    print("It's FREEZING outside!")
    print("It's Sunny!")
elif 28 > temp > 0 and not is_raining:
    print("It's WARM outside!")
    print("It's Sunny!")
elif temp >= 28 and is_raining:
    print("It's HOT outside!")
    print("It's Raining!")
elif temp <= 0 and is_raining:
    print("It's FREEZING outside!")
    print("It's Raining!")
elif 28 > temp > 0 and is_raining:
    print("It's WARM outside!")
    print("It's Raining!")