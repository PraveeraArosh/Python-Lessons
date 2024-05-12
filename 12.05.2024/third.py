username = str(input("What is username ?"))
password = str(input("Enter password"))

if (username.lower().strip()) == "tom" and (password == "123"):
    print("Correct")
else:
    print("This is incorrect")
