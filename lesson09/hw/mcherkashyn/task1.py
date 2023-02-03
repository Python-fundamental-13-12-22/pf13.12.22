import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def valid_email(email):
    try:
        if (re.fullmatch(regex, email)):
            print("Email is valid")
        else:
            raise Exception
    except Exception:
        print("Email is not valid")

valid_email("hello@gmail.co5")
