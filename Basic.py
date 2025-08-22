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


# Write a program to check if a number is even or odd..

num =  int(input("Enter the Number : "))
if num%2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd." )

# Reverse a String

inputStr = input("Reverse String : ")

print(inputStr[::-1])


def StringRevers(s):
    reversedstr = ""
    for char in s:
        reversedstr = char + reversedstr
    return reversedstr

inputStr = input("Reverse String : ")
RevStr = StringRevers(inputStr)

print(RevStr)



# Check Palindrome

def check_pelindrome(p):
    newstr = str(p)
    pelindrome_num = newstr[::-1]
    return int(pelindrome_num)

num  = int(input("Enter Number to Check Pelindrome or not : "))
callfun = check_pelindrome(num)
if callfun == num:
    print(f"{num} is Pelindrome")
else:
    print(f"{num} is not Pelindrome")

    

def Check_pelindrom(p):
    rev = 0
    temp = p
    while temp > 0:
        digit =temp%10 
        rev = rev *10 + digit
        temp = temp//10
    print(rev)


Check_pelindrom(121)

'''


