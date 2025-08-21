# Swap two variables.
'''
var1 = 12
var2= 'Ram'
print(f"Swap Two Variable :\n a : {var1} \n b: {var2}" )
temp = var1
var1 = var2
var2 = temp
print(f"Swap Two Variable :\n a : {var1} \n b: {var2}" )
'''


# Swap two variables without using a third variable.
'''
method 1
a = 5
b = 10
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )
a,b = b,a
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )

Method 2

a = 20 
b = 30
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )
a = a+b
b = a-b
a = a-b
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )


method 3

a = 2 
b = 5
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )
a = a^b
b = a^b
a= a^b
print(f"Swap Two Variable :\n a : {a} \n b: {b}" )
'''

# Write a program to check if a number is even or odd.
'''
num =  int(input("Enter the Number : "))
if num%2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd." )
'''

