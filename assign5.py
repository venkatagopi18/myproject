# add a key to the dictionary
a={0:10,1:20}
a[2]=30
print(a)

a.update({2:30})
print(a)


# checking a key in the dictionary or not

a={"val1":"10","val2":"20"}
if "val1" in a:
    print(True)
else:
    print(False)


# iterating for loop in dictionary

a={"val1":10,"val2":20,"val3":30}
for key in a.keys():
    print(key)
for value in a.values():
    print(value)
for item in a.items():
    print(item)


# creating dictionary from a string and counting duplicate elements

string='marolix technology'
dic={}
for i in string:
    dic[i]=string.count(i)
print(dic)


# printing a dictionary using keys and values

dic={}
for i in range(1,15+1):
    dic[i]=i**2
print(dic)


# sum of all the items

dic={'a':10,'b':20,'c':30}
print(sum(dic.values()))

# accecing keys in dictionary

dic={"physics":75,"maths":80,"chemistry":70}
for i in dic.keys():
    print(i)


# removing key in dictionary

d1={'a':100,'b':200,'c':300}
d1.pop('a')
print(d1)


# merging two dictionaries

d1={'a':100,'b':200,'c':300}
d2={'d':400,'e':500,'f':600}
d1.update(d2)
print(d1)

