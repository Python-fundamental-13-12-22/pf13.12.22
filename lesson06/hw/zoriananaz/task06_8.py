"""8. Напишіть функцію `number_of_uc_lc`, яка приймає рядок і обчислює кількість великих і малих літер.
повертає dict `{"uc":n, "lc":m}`."""


def number_of_uc_lc(str_ent):
    str_list = list(str_ent)
    uc = 0
    lc = 0
    for i in str_list:
        if i.isupper():
            uc += 1
        elif i.islower():
            lc += 1
    dict_res = {"uc": uc, "lc": lc}
    return dict_res


print(number_of_uc_lc("My nAme is..."))
