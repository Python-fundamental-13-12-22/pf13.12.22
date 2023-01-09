def number_of_uc_lc(s):
    a = {}
    sum_lower = 0
    sum_upper = 0
    for i in range(len(s)):
        if s[i].islower():
            sum_lower += 1
        elif s[i].isupper():
            sum_upper += 1
    a["uc"] = sum_upper
    a["lc"] = sum_lower
    return a
s = 'ddetLgt5dH5sdsdsdsdWewe'
print(number_of_uc_lc(s))
