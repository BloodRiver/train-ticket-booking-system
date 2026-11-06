from utilities import check_email_validity

email = input("Enter your email: ")

if check_email_validity(email) == True:
    password = input("Enter your password: ")
else:
    print("Invalid email")
