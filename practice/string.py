username = input("Enter a username: ")

if len(username) > 12 :
    print ("Your username can't be more than 12 haracters")
elif not username.find(" ") == -1:
    print ("Your username can't contain spaces")
elif not username.isalpha():
    print ("Your username can't contain numbers")
else:
    print(username)
