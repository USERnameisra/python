username = input("enter a username: ")






if len(username) > 12:
    print("your username is more than 12 try again")
elif not username.find(" ") == -1:
    print("may space")
elif not username.isalpha():
    print("may number")
else:
    print(f"welcome {username}")


