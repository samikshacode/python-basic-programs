import re
def password_streangth_checker(password):
    strength=0

    if len(password) >=8:
        strength+=1

    else:
        return "Weak password(password must be atleast 8 characters long)"

    if re.search(r'[A-Z]',password):
        strength+=1

    if re.search(r'[a-z]',password):
        strength+=1

    if re.search(r'[!@$%&*]',password):
        strength+=1

    if strength==5:
       return "Very Strong"
    elif strength==4:
        return "Strong"
    elif strength==3:
        return "Moderate"
    else:
        return "Weak password(password must contain atleast ons special character,one uppercase and lowercase letter and digits)"       
    
password=input("Enter the password to check its strength:")
print(password_streangth_checker(password))
