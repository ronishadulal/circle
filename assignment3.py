#sort given list without using python method
a = [54, 1, 12, 99, 20, 13, 5, 100]
aa = []
while a:
    minimum = a[0]
    for x in a:
        if x < minimum:
            minimum = x
    aa.append(minimum)
    a.remove(minimum)
print(aa) 


#create a number whose digits are the elements of list
A = [4,2,3]
for i in A :
    print(i, end="")
