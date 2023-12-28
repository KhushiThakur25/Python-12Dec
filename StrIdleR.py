Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> st = "hello world"
>>> st[5]
' '
>>> st[4]
'o'
>>> st[2:6]
'llo '
>>> st[2,6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    st[2,6]
TypeError: string indices must be integers, not 'tuple'
>>> st[2:7]
'llo w'
>>> st[1:9:2]
'el o'
>>> a = "k"
>>> type(a)
<class 'str'>
>>> "hello" == "Hello"
False
>>> st = "this iS PythON LAnguage"
>>> st.lower()
'this is python language'
>>> st
'this iS PythON LAnguage'
print(st.lower())
this is python language
st.upper()
'THIS IS PYTHON LANGUAGE'
st.capitalize()
'This is python language'
st.title()
'This Is Python Language'
st.swapcase()
'THIS Is pYTHon laNGUAGE'
"hello".casefold() == "Hello".casefold()
True
st = "     this iS PythON LAnguage"
st.strip()
'this iS PythON LAnguage'
st = "     this iS PythON LAnguage*****"
st.rstrip()
'     this iS PythON LAnguage*****'
st.rstrip("*")
'     this iS PythON LAnguage'
st.endswith("age")
False
st.rstrip("*")
'     this iS PythON LAnguage'
st.startswith("this")
False
st.strip()
'this iS PythON LAnguage*****'
st.startswith("this")
False
st = st.strip()
st.startswith("this")
True
st.count("i")
2
st.count("a")
1
st = st.lower()
st.count("a")
2
len(st)
28
st.index("i")
2
st.rindex("i")
5
st.index("z")
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    st.index("z")
ValueError: substring not found
st.find("z")
-1
st.split()
['this', 'is', 'python', 'language*****']
st.partition()
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    st.partition()
TypeError: str.partition() takes exactly one argument (0 given)
st.partition("is")
('th', 'is', ' is python language*****')
st.islower()
True
st.isupper()
False
st.iscapitalize()
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    st.iscapitalize()
AttributeError: 'str' object has no attribute 'iscapitalize'. Did you mean: 'capitalize'?
st.istitle()
False
st = "hello world"
st.replace("l","o")
'heooo worod'
st.replace("l","o",5)
'heooo worod'
st.replace("l","o",3)
'heooo worod'
st.replace("l","o",1)
'heolo world'
st = "this is a python"
st = st.split()
st
['this', 'is', 'a', 'python']
" ".join(st)
'this is a python'

