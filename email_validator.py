def email_validation(email):
    if "@" in email:
        string=email.split("@")#dividing the string into two parts using @ symbol as seperator
        if len(string)==2:
            username, domain=string
            if"." in domain:
                return True
            else:
              return False  
            
result=email_validation("samikshagmail.com")
if result==True:
    print("Email is valid")
else:
    print("Email is not valid")




