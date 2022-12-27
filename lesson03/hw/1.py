#HW1.1
s1="""Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""
s2=s1.upper()
print(s2)

#HW1.2
a=s1.count("better")
b=s1.count("never")
c=s1.count("is")
words=a+b+c

#HW1.3
if s1:
    print("Number of words: ", words)

    new_s1=s1.replace("i", "&")
    print(new_s1)

#HW2.1
def getSum(n):

  sum=0
  for digit in str(n):
    sum += int(digit)
  return sum

n=8765
print(getSum(n))

#HW2.2
number=8765
reverse_number=0
while number>0:
  reverse_number= reverse_number*10+number%10
  number//=10
print(reverse_number)

#HW2.3
number=8765
digit={int(d) for d in str(number)}
sorted_number=sorted(digit)
print(sorted_number)

#HW3
number1=8
number2=7
number1,number2=number2,number1
print(number1)
print(number2)