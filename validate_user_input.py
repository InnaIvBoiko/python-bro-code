# username is no more than 12 characters long
# username must not contain any spaces
# username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    print("Username must be no more than 12 characters long.")
elif " " in username:
    print("Username must not contain any spaces.")
elif any(char.isdigit() for char in username):
    print("Username must not contain digits.")
else:
    print(f"Welcome {username.capitalize()}!")