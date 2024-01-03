Python 3.11.6 (tags/v3.11.6:8b6ee5b, Oct  2 2023, 14:57:12) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
li = [1,2,6.1,"ram",True]
type(li)
<class 'list'>
li = {1,2,6.1,"ram",True}
type(li)
<class 'set'>
print(li)
{1, 2, 6.1, 'ram'}
li = [1,2,6.1,"ram",True]
print(li)
[1, 2, 6.1, 'ram', True]
li = list()
li
[]
li[0] = 56
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    li[0] = 56
IndexError: list assignment index out of range
li = [1,2,3,4,5]
li[0] = 56
li
[56, 2, 3, 4, 5]
li[4]
5
del li[2]
li
[56, 2, 4, 5]
li.append(6)
li
[56, 2, 4, 5, 6]
li.insert(3,2)
li
[56, 2, 4, 2, 5, 6]
li.extend([2,3,56,4])
li
[56, 2, 4, 2, 5, 6, 2, 3, 56, 4]
li.append([65,98,78])
li
[56, 2, 4, 2, 5, 6, 2, 3, 56, 4, [65, 98, 78]]
len(li)
11
li.count(2)
3
for i in li:
    print(i)

56
2
4
2
5
6
2
3
56
4
[65, 98, 78]
>>> max(li)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    max(li)
TypeError: '>' not supported between instances of 'list' and 'int'
>>> li = [1,2,3,4,5]
>>> max(li)
5
>>> min(li)
1
>>> li[1:4]
[2, 3, 4]
>>> li[::-1]
[5, 4, 3, 2, 1]
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
>>> li = [1,2,3,4,5]
>>> li.reverse()
>>> li
[5, 4, 3, 2, 1]
