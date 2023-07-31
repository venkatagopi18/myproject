# positive or negative
a=int(input())
if a>0:
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
if a>35:
    print("venkat is pass")
else:
    print("venkat is fail")

# eligible for vote
a=int(input())
if a>18:
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