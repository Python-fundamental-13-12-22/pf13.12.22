def number_of_uc_lc(row):
    count = 0
    count2 = 0
    for i in row:
        if i.isupper():
            count = count + 1
        if i.islower():
            count2 = count2 + 1
    dict = {"uc":count, "lc":count2}
    return dict

print(number_of_uc_lc("Hello World"))
