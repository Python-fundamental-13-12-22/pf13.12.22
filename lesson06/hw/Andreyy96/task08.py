def number_of_uc_lc(text):
    sum_uc = 0
    sum_lc = 0
    for i in range(0, len(text)):
        if text[i].isupper():
            sum_uc += 1
        elif text[i].islower():
            sum_lc += 1
        else:
            continue
    dict_uc_lc = {"uc": sum_uc, "lc": sum_lc}

    return dict_uc_lc

text = str(input('Введите строку'))
print(number_of_uc_lc(text))
