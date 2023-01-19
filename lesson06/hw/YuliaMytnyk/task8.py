def number_of_uc_lc(string):
    uc=0
    lc=0
    for symbol in string:
        if symbol.isupper():
            uc+=1
        elif symbol.islower():
            lc+=1
    return {"uc":uc,"lc":lc}
string=input("Enter a text: ")
print(number_of_uc_lc(string))
