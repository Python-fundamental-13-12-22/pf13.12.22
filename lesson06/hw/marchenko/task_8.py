# TASK 8

def number_of_uc_lc(string):
    uc = 0
    lc = 0
    for c in string:
        if c.isupper():
            uc += 1
        elif c.islower():
            lc += 1
    print(uc, lc)
    return {"uc": uc, "lc": lc}

