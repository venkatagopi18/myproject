# string
a="venkat"
a='venkat'

# indexing method
a=input("string:")
print(a[2])
print(a[3])
print(a[5])
print(a[-5])
print(a[-1])

# slicing
a=input()
print(a[0:4])
print(a[3:])
print(a[::2])
print(a[:3:-2])

# string concatination
a=input("enter string1:")
b=input("enter string2:")
print(a+b)

# string repeatation
a=input("repeat")
print(a*2)
print(a*4)
print(a*5)
print(a*10)

# find length of string
a=input("str len")
l=len(a)
print(a)

string printing
a=input()
l=len(a)
i=0
while i <l:
    print(a[i],end=" ")
    i=i+1
while i<1:
    print(a[i])
    i=i+1
reverse printing
a=input()
for i in a[::-1]:
    print(i,end=" ")
a=input()
str=""
for i in a:
    str=i+str
    print(str)

# membership cheching
a=input()
print("v" in a)
print("k" in a)
print("s" in a)
print("j" in a)

a=input()
b=input()
if b in a:
    print("found")
else:
    print("not found")

a=input()
b=input()
if b not in a:
    print("True")
else:
    print("false")

# removing space
a=input()
print(a.strip())

a=input()
print(a.rstrip())

a=input()
print(a.lstrip())

# camparing strings
a=input()
b=input()
if a==b:
    print("equal")
else:
    print("not equal")

str=input()
str1=input()
if str<=str1:
    print("str1 is greater")
else:
    print("str is greater")