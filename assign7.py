# recursion
# adding elements ny using recursion

def recursive_adding(x):
    if x==1:
        return 1
    else:
        return(x+recursive_adding(x-1))
n=10
res=recursive_adding(list(n))
print(res)

# factorial 
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
k=10
kres=factorial(k)
print(kres)


# lambda function
# multiplying arguments by using lambda function

args=lambda a,b,c:a*b*c
print(args(10,15,20,))

# squares of a value by using lambda function

val=lambda a:a**2
print(val(25))

# given are equal or not

x=lambda a,b:"equal" if(a==b) else "not equal"
print(x(2,2))
print(x(20,30))


# filter() function

# finding positive elements by using filter function

def positive(a):
    if a>=0:
        return True
    else:
        return False
t=(2,-2,4,-5,-6,7,8,)
t1=tuple(filter(positive,t))
print(t1)

# finding bigger than 5

def bigger_than_5(a):
    if a>5:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8]
l1=list(filter(bigger_than_5,l))
print(l1)

# finding numbers by using filter 

def numbers(a):
    if str(a).isdigit():
        return True
    else:
        return False
l=[1,"venkat",2,3]
l1=list(filter(numbers,l))
print(l1)







