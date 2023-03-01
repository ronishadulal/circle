# set elements must be immutable
s1 = {1,2,3}
s1.add(4)
print(s1)
s1.update([4,5,6])
print(s1)
s1.discard(4) # gives none as output incase of invalid number
print(s1)
s1.clear()
print(s1)
s2 = {4,5,6,7}
s2.remove(5) #gives error
print(s2)
s3 = {7,8,9}
s3.pop()
print(s3)

a = {1,2,3,4}
b= {4,5,6}
print(a.intersection(b))
print(a.union(b))
print(a.difference(b))
print(a.isdisjoint(b))
print(a.symmetric_difference(b))

#conditions
a = int(input("enter value for a "))
b = int(input("enter value for b "))
c = int(input("enter value for c "))
if a > b and a > c :
    print(a, 'is the greatest')
elif b > c and b > a :
    print( b,'is the greatest')
else:
    print(c, "is the greatest") 
    # or print(f"{c} is the greatest")       

#loop
for i in range(10): # it ranges from 0 to 9
    print(i)
