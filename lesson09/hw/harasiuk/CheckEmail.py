import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class MyError(Exception):
    pass


def valid_email(email):
    try:
        if (re.fullmatch(regex, email)):
            print("Email is valid")
        else:
            raise MyError
    except MyError:
        print("Email is not valid")


valid_email("trafik@ukr.tel.com") #output: "Email is valid"
valid_email("trafik@ukr_tel.com") #output: "Email is not valid"
valid_email("tra@fik@ukr.com") #output: "Email is not valid"
valid_email("ownsite@our.c0m") #output: "Email is not valid"
