#part1
s1 ="""Beautiful is better than ugly.
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
b=s1.count("better")
c=s1.count("never")
d=s1.count("is")
words=b+c+d
if s1:
    print("Number of words:", words)
    text2=s1.replace("i","&")
    print(text2)
#part2
def getSum(a):

  sum=0
  for digit in str(a):
    sum += int(digit)
  return sum

a=777
b=888
c=999
d=987
print(getSum(a))
print(getSum(b))
print(getSum(c))
print(getSum(d))
number = 123456789
reverse_number=0
while number >0:
  reverse_number=reverse_number*10+number %10
  number //=10
print(reverse_number)
number=9241536780
digit={int(a)for a in str(number)}
sorted_number=sorted(digit)
print(sorted_number)
#part3
b=7
d=1
b,d = d,b
print(b)
print(d)
#this homework motivated me thx:)