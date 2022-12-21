text = '''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
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
Namespaces are one honking great idea -- let's do more of those!'''

count_world = f'Количество "better" в переменой {text.count("better")}'
print(count_world)

count_world = f'Количество "never" в переменой {text.count("never")}'
print(count_world)

count_world = f'Количество "is" в переменой {text.count("is")}'
print(count_world)
print()

upper_text = text.upper()
print(upper_text)

change = "&".join(text.split("i"))
print(change)