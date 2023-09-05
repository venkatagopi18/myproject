# counting upper lower cases
def counting_upper_lower_cases(string):
    upper=0
    lower=0
    for i in string:
        if i.isupper():
            upper=upper+1
        elif i.islower():
            lower=lower+1
    print(upper)
    print(lower)
string="The quick Brow Fox"
counting_upper_lower_cases(string)



##printing distinct elements in the list

def sorting_lst(l):
    new_lst=[]
    for i in l:
        if i not in new_lst:
            new_lst.append(i)
    print(new_lst)

l=[1,2,3,3,3,3,4,5]
sorting_lst(l)


# pangram or not

def pangram_r_not(k):
    new_set=set(k)
    if len(new_set)==26:
        print("pangram")
    else:
        print("not pangram")

k=input()
pangram_r_not(k)

#squares of the 1 to 10

def squares_of_lst(k,l):
    new_lst=[]
    for i in range(k,l+1):
        new_lst.append(i**2)
    print(new_lst)

k=int(input())
l=int(input())
squares_of_lst(k,l)


# sum all the elements in list

def sum_of_elements(*lst):
    sum=0
    for i in lst:
        sum=sum+int(i)
    print(sum) 
sum_of_elements(8,2,3,0,7)
