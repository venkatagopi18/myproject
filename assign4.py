# merging two lists
a=[10,20,30,40,]
b=[1,2,3,4,5,6]
print(a+b)

a=[10,20,30,40,]
b=[1,2,3,4,5,6]
a.extend(b)
print(a)

# sum of arrays
a=[10,20,30,40]
k=0
for i in a:
    k=k+i
print(k)

# even numbers in list
a=[1,2,3,40,77,82,647,8]
k=[]
for i in a:
    if i%2==0:
         k.append(i)
print(k)

# odd numbers in list
a=[1,2,3,40,77,82,647,8]
j=[]
for i in a:
    if i%2 !=0:
        j.append(i)
print(i)

# deleting element in given list
a=[1,2,3,40,77,82,2,647,8]
a.remove(3)
print(a)

# inserting element in given list at end 
a=[1,2,3,40,77,82,2,647,8]
a.append(20)
print(a)

# inserting element in given list 
a=[1,2,3,40,77,82,2,647,8]
a[5]=99
print(a)

# check the size of two lists are same or not
a=[10,20,30,40,50,60]
b=[60,70,80,90,100]
if len(a)==len(b):
    print("size of the a and b are same")
else:
    print("size of the a and b are not same")
