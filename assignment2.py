#calculate difference between number and 17 print double the output if number is greater than 17
n = int(input("enter any number"))
d = n - 17
if n > 17 :
    print(d * 2)
else: 
    print(d)    
#to check prime number
a = int(input("enter any number"))
count = 0
i = 1
while i <= a:
     if a % i == 0:
      count = count + 1
     i = i + 1  
if count == 2:
    print( a,"is a prime number")
else:
    print(a, "is not a prime number")  

#to compute the value of n+nn+nnn....
n = int(input(" enter any number "))
nn = int('%s%s'%(n,n))
nnn = int('%s%s%s'%(n,n,n))
print(n + nn + nnn)


