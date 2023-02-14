import re
def valid_email(email):
    try :
        pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'

        match=re.match(pattern,email)
        if match:
            return f"Email ({email}) is valid"
        else:
            raise ValueError
    except ValueError:
        return f"Email ({email}) is not valid"
print(valid_email("trafik@ukr.tel.com"))
print(valid_email("trafik@ukr_tel.com"))
print(valid_email("tra@fik@ukr.com"))
print(valid_email("ownsite@our.c0m"))
