for i in range (1,11):
  if i % 2 == 0:
   print(i, "it is an even number")
  else:
   print( i,"it is an odd number")   

for i in range (1, 31):
 if i % 3 == 0 and i % 5 == 0:
   print('FizzBuzz', end="")
   break 
 elif i % 3 == 0 :
   print('Fizz', end="")
 elif i % 5 == 0 :
  print('Buzz', end="") # end = "" to get result in  a single line
 else:
   print(i, end = "")

for x in [1, 2, 'a']:
  print(x)

for y in "hey":
  print(y)
