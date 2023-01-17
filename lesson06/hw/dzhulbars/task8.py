def count_uc_lc(word):
    upper_count=0
    lower_count=0
    for word in word:
        if word.isupper():
            upper_count+=1
        elif word.islower():
            lower_count+=1
    return {"Upper":upper_count,"Lower":lower_count}
word=input("Enter a word: ")
result=count_uc_lc(word)
print(f"The result: {result}")

