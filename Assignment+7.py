# username= input("Enter your name: ")
# print(f"Hello {username}")


# # 2
# age = input("How old are you ?: ")
# print(f"You are {age} years old")

# # 3
# fav_color= input("What is your favorite color? ")
# print(f"Your avourite color is {fav_color}")

# # 4
# text= input("Type in a word to check if it is a palindrome: ")
# check=text[::-1]
# print(check)
# if check==text:
#     print(f"The word {check} is a palindrome")
# else:
#     print("Not a palindrome")

# # 5
# from getpass import getpass
# pwd = getpass("Hi, input your password 9NOTE: your password should not be less than 8 characters nor more than 30 characters, any violation will be flagged!")

# if len(pwd)<8:
#     is_valid=False
#     print(f"It is {is_valid} that the password fulfils the criteria, because it is less than 8 characters")
# elif len(pwd)>=8 and len(pwd)<=30 :
#     is_valid=True
#     print(f"It is {is_valid} that the password fulfils the criteria beacuse it is between 8-30 characters")
# elif len(pwd)>30:
#     is_valid=False
#     print(f"It is {is_valid} that the password fulfils the criteria because it exceeds 30 characters")

#     # 6
# weight=int(input("Enter your weight in kilograms: "))
# height=float (input("Enter your weight in meters: "))
# BMI = weight/(height**2)
# print(f" Your BMI is {BMI}")


# -----------------ASSIGNMENT 1-----------------------------
# 11
x,y,z = "Orange ","Banana ","Cherry."  
print(x,y,z)

# 12
age,name,is_student = 10,"John",True
print(age,name,is_student)

# 13
x,y=5,10
print(f"Values x and y: {x} and {y}")
y,x =5,10
print(f"Swapped values x and y: {x} and {y}")

# 14
numberlist=[1,2,3]
a,b,c=numberlist
print(a,b,c)

# 15
height =float(1.35)
print(height)

# 16
# a
print(bool(""))  
# False

# b
print(bool(123))
# True

# c
print(bool(["apple","cherry","banana"]))
# True

# d
print(bool(False))
# False

# e
print(bool(None))# False

# f
print(bool(0))
# False

# g
print(bool("abc"))
# True

# h
print(bool(()))
# False

# i
print(bool({}))
# False

# j
print(bool([]))
# False