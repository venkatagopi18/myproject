# removing character in string

str=input()
print(str.replace("a"," "))

# printing palindrome or not

a=input()
l=len(a)
if a[:int(l/2)]==a[int(l/2):]:
    print("a is palindrome")
else:
    print("a is not a palindrome")

# finding vowel or consonant

str=input()
vow=("a","e","i","o","u","A","E","I","O","U")
if str in vow:
    print("vowel")
else:
    print("consonant")

replacing given character in space
str=input()
print(str.replace(" ",str))

# count of alphabets,digits,special characters
str=input()
alcount=0
dicount=0
spcount=0
for k in str:
    if k.isalpha():
        alcount=alcount+1
    elif k.isdigit():
        dicount=dicount+1
    else:
        spcount=spcount+1
print("alphabets: ",alcount)
print("digits: ",dicount)
print("special characters: ",spcount)

# removing blank spaces in string
a=input()
print(a.replace(" ",""))

# find sum of integers
a=input()
sum=0
for i in a:
    sum =sum+int(i)
print(sum)

# removing repeated charecter
a=input()
print(a.replace("d",""))
        
# count of given character
a=input()
print(a.count("v"))

# check anagram or not
a=input()
b=input()
if sorted(a)==sorted(b):
    print("the strings are anagrams")
else:
    print("the strings are not anagrams")

# sort characters
a=input()
print(sorted(a))