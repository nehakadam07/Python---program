# Q4 - Login Security System

correct_password = "python123"
for attempt in range(1, 4):
    password = input("Enter password: ")

    if password == correct_password:
        print("Login Successful")
        break
    else:
        print("Incorrect Password")

        if attempt == 3:
            print("Account Locked")
        else:
            print("Attempts remaining:", 3 - attempt)