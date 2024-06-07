email = input("Email Address : ")

def validate_email(email:str)->bool:
    if email.count('@') ==1:
        split_email = email.split('@')
        if len(split_email[0]) > 3 and len(split_email[1]) > 3:
            return True
        else:
            False
    else:
        False

print(f"your email is {validate_email(email)}")