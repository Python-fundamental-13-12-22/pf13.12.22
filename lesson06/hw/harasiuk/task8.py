def number_of_uc_lc(str):
    uc = 0
    lc = 0
    for i in range(0, len(str)):
        if str[i].isupper():
            uc = uc + 1
        else: lc = lc + 1
    dict = {"uc":uc, "lc":lc}
    return dict


str = input("input string\n")
print(number_of_uc_lc(str))
