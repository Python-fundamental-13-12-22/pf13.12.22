import re


class Myclass(Exception):
    pass


def valid_email(email):
    try:
        reg_ex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        if re.match(reg_ex, email):
            print(f"Email is valid")
        else:
            raise Myclass
    except Myclass:
        print(f"Email is not valid")


valid_email("trafik@ukr.tel.com")
valid_email("trafik@ukr_tel.com")
valid_email("tra@fik@ukr.com")
valid_email("ownsite@our.c0m")
