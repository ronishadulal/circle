#sort given list without using python method
a = [54, 1, 12, 99, 20, 13, 5, 100]

for x in range(0,len(a)):
    for y in range (x +1, len(a)):
        if (a[x]>a[y]):
            a[x],a[y]=a[y],a[x]
print(a)         


#create a number whose digits are the elements of list
A = [4,2,3]
for i in A :
    print(i, end="")
