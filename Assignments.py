# positive or negative
a=int(input())
if a>=0:
    print("positive")
else:
    print("negative")

# find greater
b=int(input())
a=int(input())
if a>b:
    print("a is greater")
else:
    print("not greater")

# repeating string
a=input("enter string")
print(a*5)


# half of string
a=input()
l=len(a)
print(a[0:int(l/2)])
print(a[int(l/2):])

# pass or fail
a=int(input())
if a>=35:
    print("venkat is pass")
else:
    print("venkat is fail")

# eligible for vote
a=int(input())
if a>=18:
    print("eligible for vote")
else:
    print("not eligible")

# find square
l=int(input())
b=int(input())
if l==b:
    print("it is a square")
else:
    print("not a square")

# even and odd numbers
a=int(input())
for i in range(a):
    if i%2==0:
        print(i)
a=int(input())
for j in range(a):
    if j%2==1:
        print(j)

# printing patterns
# 1
a=int(input())
for i in range(a):
    print("* "*i)

# 2
a=int(input())
for i in range(1,a):
    for j in range(1,i+1):
        print(j)
    print()
# 3
a=int(input())
for i in range(a):
    print("222 "*i)

# assignment2

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




