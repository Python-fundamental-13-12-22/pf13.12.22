import string
class CheckEmail:
    def __init__(self, string_email= ''):
        self.string_email = string_email
    def valid_email(self):
        self.string_email.split('@')
        try:
            user_info = self.string_email.split('@')[0]
            domain_info = self.string_email.split('@')[1]
            email_dict = dict.fromkeys(string.ascii_lowercase, 0)
            email_dict['.'] = '0'
            email_dict = tuple(email_dict)
            k = 0
            for i in range(0,len(domain_info)):
                if domain_info[i] in email_dict:
                    k+= 1
            if len(domain_info) == k and '.' in tuple(domain_info):
                result = "Email is valid"
            else:
                result = "Email is not valid"
            return result
        except:
            result = 'Error, please enter correct e-mail'
            return result



input_email = str(input('Please enter your email '))
email0 = CheckEmail(input_email)
print(email0.valid_email())
input_email = str(input('Please enter your email '))
email1 = CheckEmail(input_email)
print(email1.valid_email())
input_email = str(input('Please enter your email '))
email2 = CheckEmail(input_email)
print(email2.valid_email())
input_email = str(input('Please enter your email '))
email3 = CheckEmail(input_email)
print(email3.valid_email())