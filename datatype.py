#dic [] error
# method none
print(bool(''))
print(bool("helloworld"))
str1 = "hello world"
x = slice(2, 5)
print(str1[x])
print(len(''))
print(len("hello world"))
str2 = "hello World"
print(str2.capitalize())
print(str2.lower())
print(str2.upper())
print(str2.title())
str3 = "cookie cutter"
str4 = "cut"
str5 = "Cut"
print(str3.find(str4))
print(str3.find(str5))
str6 = 'hip hip hurray'
print(str6.replace('hip', 'Hip'))
print(str6.replace('hip', 'Hip', 1))
str7 = 'hello world'
print(str7.split())
pets = 'cat, dog, mouse'
print(pets.split(','))
str_ist = ['hello', 'world']
print(''.join(str_ist))
pets = ['cats', 'dog', 'mouse']
print(','.join(pets))

#programiz.com
#geeks for geeks
#corey schafer
#formatting
#first method f-string
a = 'broadway'
m = f"i study at {a}"
print(m)
#second method
a ='i am %s and i am %d'%('ronisha', 18)
print(a)
#third method
b = 'i am {} and i am {} years old.'.format('ronisha', 18)
print(b)
print('i have {0}, {2} and {1} in my bag.'.format('book','pen','pencil'))
print('{a}, {b}, {c}'.format(a='foo', b='bar', c ='baz'))
print(f"{{2+3}}")
print(f"{{{2+3}}}")




