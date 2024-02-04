# challenge 15

import re

def is_invalid_email(email):
    # Regular expression for validating email address
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    # Use re.match to check if the email matches the pattern


    if re.match(pattern, email):

        return "is valid email"
    
    else:
        return "invalid email"

email1 = "example@.com"
email2 = "example.com"
email3 = "example@email.com"
email4 = "example@gmail.com"

print(f"{email1} {is_invalid_email(email1)}")
print(f"{email2} {is_invalid_email(email2)}")
print(f"{email3} {is_invalid_email(email3)}")
print(f"{email4} {is_invalid_email(email4)}")
    