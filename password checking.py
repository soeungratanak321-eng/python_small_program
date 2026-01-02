password = "admin12345"
userpassword = input("Enter your password: ")
while password != userpassword:
    print("Wrong please try again")
    userpassword = input("Enter your password: ")
else: print("correct")

