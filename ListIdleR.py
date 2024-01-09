Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: C:/Python312/ListMthdR.py
None
lists = [65,84,21,20,98,2,3,98,24]
lists.sort()
lists
[2, 3, 20, 21, 24, 65, 84, 98, 98]

===== RESTART: C:/Python312/ListMthdR.py ====
[2, 3, 20, 21, 24, 65, 84, 98, 98]
>>> 
===== RESTART: C:/Python312/ListMthdR.py ====
[98, 98, 84, 65, 24, 21, 20, 3, 2]
>>> lists = [65,84,21,20,98,2,3,98,24]
>>> lists.reverse()
>>> lists
[24, 98, 3, 2, 98, 20, 21, 84, 65]
>>> li = lists
>>> li
[24, 98, 3, 2, 98, 20, 21, 84, 65]
>>> li[0] = 56
>>> li
[56, 98, 3, 2, 98, 20, 21, 84, 65]
>>> lists
[56, 98, 3, 2, 98, 20, 21, 84, 65]
>>> m = li.copy()
>>> li
[56, 98, 3, 2, 98, 20, 21, 84, 65]
>>> m
[56, 98, 3, 2, 98, 20, 21, 84, 65]
>>> m[0] = 111
>>> m
[111, 98, 3, 2, 98, 20, 21, 84, 65]
>>> li
[56, 98, 3, 2, 98, 20, 21, 84, 65]
