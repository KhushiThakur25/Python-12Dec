Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Python is a programming language..")
Python is a programming language..
a = 10
print(a)
10
a = 50
print(a)
50
a = "khushi"
print(a)
khushi
a = 10
b = 30
a+b
40
a-b
-20
a*b
300
b/a
3.0
b//a
3
b%a
0
b**a
590490000000000
a += 2
a
12
b -= 15
b
15
a *= 2
a
24
b /= 3
b
5.0
b //= 3
b
1.0
a
24
b
1.0
b = 12
a > b
True
a < b
False
a == b
False
a != b
True
x,y,z = 12,10,8
x
12
y
10
z
8
a,b,c=1,2
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a,b,c=1,2
ValueError: not enough values to unpack (expected 3, got 2)
 a = 10
 
SyntaxError: unexpected indent
a = 10
b = 4
a & b
0
b = 9
a & b
8
a ^ b
3
x = 10
x+1
11
x
10
x = x + 1
x
11
x = "String"
x[0]
'S'
x[3]
'i'
>>> del x[0]
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    del x[0]
TypeError: 'str' object doesn't support item deletion
>>> x[0] = "p"
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x[0] = "p"
TypeError: 'str' object does not support item assignment
>>> tup = (1,2,3,4,5)
>>> type(tup)
<class 'tuple'>
>>> type(x)
<class 'str'>
>>> tup[1]
2
>>> del tup[1]
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    del tup[1]
TypeError: 'tuple' object doesn't support item deletion
>>> tup[2] = 6
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tup[2] = 6
TypeError: 'tuple' object does not support item assignment
