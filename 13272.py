Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=[1,2,3]
type(a)
<class 'list'>
a.append(4)
print a
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
print(a)
[1, 2, 3, 4]
a.insert(3, 6)
print(a)
[1, 2, 3, 6, 4]
remove.a(3)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    remove.a(3)
NameError: name 'remove' is not defined
a.remove(3)
print (a)
[1, 2, 6, 4]
a.pop(3)
4
print (a)
[1, 2, 6]
a.append(5)
print(a)
[1, 2, 6, 5]
a.pop
<built-in method pop of list object at 0x0000025BF2551280>
print(a)
[1, 2, 6, 5]
a.pop()
5
a.sort()
print (a)
[1, 2, 6]
a.append(4,2,9,8)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.append(4,2,9,8)
TypeError: list.append() takes exactly one argument (4 given)
>>> a.append(8)
>>> a.append(7)
>>> print (a)
[1, 2, 6, 8, 7]
>>> a.sort()
>>> print (a)
[1, 2, 6, 7, 8]
>>> a.sort(reverse=true)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    a.sort(reverse=true)
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> a.sort (reverse = True)
>>> print (a)
[8, 7, 6, 2, 1]
>>> 
>>> 
>>> a={}
>>> 
>>> type(a)
<class 'dict'>
>>> a = {"1": "Ford","2": "BMW","3": "Mercedes"}
>>> print{a}
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> print(a)
{'1': 'Ford', '2': 'BMW', '3': 'Mercedes'}
>>> a.copy
<built-in method copy of dict object at 0x0000025BF2552980>
>>> a.copy()
{'1': 'Ford', '2': 'BMW', '3': 'Mercedes'}
>>> a.fromkeys()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    a.fromkeys()
TypeError: fromkeys expected at least 1 argument, got 0
>>> a.fromkeys(3)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.fromkeys(3)
TypeError: 'int' object is not iterable
>>> a.get(2)
>>> print (a)
{'1': 'Ford', '2': 'BMW', '3': 'Mercedes'}
>>> a["4"]= "Tata"
>>> print (a)
{'1': 'Ford', '2': 'BMW', '3': 'Mercedes', '4': 'Tata'}
>>> {'1': 'Ford', '2': 'BMW', '3': 'Mercedes', '4': 'Tata'}
{'1': 'Ford', '2': 'BMW', '3': 'Mercedes', '4': 'Tata'}
>>> a.get("2")
'BMW'
>>> a.get("4")
'Tata'
>>> a.items()
dict_items([('1', 'Ford'), ('2', 'BMW'), ('3', 'Mercedes'), ('4', 'Tata')])
a.keys()
dict_keys(['1', '2', '3', '4'])
a.pop("2")
'BMW'





x=[1,2,3,4,5]
type(a)
<class 'dict'>

type(x)
<class 'list'>
x.index(2)
1
x[2]
3
x.insert(2,7)
print(x)
[1, 2, 7, 3, 4, 5]
x.remove(4)
print (x)
[1, 2, 7, 3, 5]

x*5
[1, 2, 7, 3, 5, 1, 2, 7, 3, 5, 1, 2, 7, 3, 5, 1, 2, 7, 3, 5, 1, 2, 7, 3, 5]

for i in x:
    print(i)

    
1
2
7
3
5
x.sort()
print
<built-in function print>
Print (x)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    Print (x)
NameError: name 'Print' is not defined. Did you mean: 'print'?
print(x)
[1, 2, 3, 5, 7]
