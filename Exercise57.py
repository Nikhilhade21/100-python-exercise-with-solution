'''Write a program to read an ASCII string and to convert it to a unicode 
string sencoded by utf-8.'''

s = input("enter:")
u = s.encode("utf-8")
print(u)