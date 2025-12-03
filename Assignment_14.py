# Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.
x= int(input("Enter a number : "))
y= int(input("Enter a number : "))

if x>0 and y>0:
       print("Both are positive")
elif (x<0) or (y<0):
       print("Only one is positive")
else:
       print("Neither is positive")

# Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order"
#  if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

x=int (input("Enter a number : "))
y= int(input("Enter a number : "))
z= int(input("Enter another number : ") )

if x <y and y<z:
    print("Increasing order")
elif x >y and y>z :
    print("Decreasing order")
elif (x >y and  y< z) or (x<y and y>z) or (x==y and y<z) or (y==z and x < z):
    print("Neither")
elif x==y and y==z:
    print(" The numbers are equal")

# Write a program that reads a string called `palindrome` supplied through user input 
# and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
str_ing =input("Enter a word : ").lower().strip()
str_check =str_ing[::-1]
print(str_check)

if str_check == str_ing:
     print(f"{str_ing} is a palindrome.")
else:
     print(f"{str_ing} is not a palindrome.")

# You have three variables: x, y, and z collected as 3 separate inputs from the user.
#  Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal"
#  if this is true. Otherwise, print "All different" or "All same" accordingly.

x= input("Enter a number : ")
y= input("Enter a number : ")
z= input("Enter another number : ") 

if x==y==z:
       print(f"{x} ,{z},and {y} are the same")
elif x==y:
       print(f"{x} and {y} are the same")
elif y==z:
       print(f"{y} and {z} are the same")
elif x==z:
       print(f"{x} and {z} are the same")
elif not x==y==z:
       print(f"All different")

# Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, 
# use if statements to check if they can form a valid triangle. Print "Valid triangle" 
# if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
x= input("Enter a number : ")
y= input("Enter a number : ")
z= input("Enter another number : ") 
total_angle =x+y+z

if (x < 0) or (y< 0 )or (z < 0):
       print("No value should be less than 0")
elif total_angle ==180 and ((x> 0) and (y>0) and(z>0)):
       print("Valid triangle")
elif total_angle ==180 and not((x> 0) and (y>0) and(z>0)):
       print("Invalid triangle")
elif total_angle >180:
       print("values cannot exceed 180")
# You have a single character variable `ch` supplied through user input. 
# Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise.
#  Assume that the input is a single alphabet character.
# Given a comma separated string input from the user of three colors color1, color2, and color3, 
# write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are,
#  otherwise print "Not all primary colors".
color1= input("Enter a color: ")
color2= input("Enter a color : ")
color3= input("Enter another color: ") 

if color1 in ["red", "blue", "yellow"] and color2 in ["red", "blue", "yellow"] and color3 in ["red", "blue", "yellow"]:
      print('All primary colors')
else:
      print("Not a primary colour")
# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". 
# Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", 
# and "System is off" if mode is "off".

mode = input("Enter your preferred mode between options: Automatic,manual or off : ").lower()
if mode == "automatic":
    print("Automatic mode activated")
elif mode == "manual":
    print("Manual mode activated")
elif mode == "off":
    print("System is off")
else:
    print("Choose from the stated option")

# Given a string `message` entered by the user, use if statements to check if the message contains any of the words
#  "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

message = input("Enter a message: ")

if ["urgent", "important", "immediate"] in message:
      print("High priority message")
elif not  ["urgent", "important", "immediate"] in message:
      print("Normal message")

# 10.	You have two variables, status1 and status2, provided through user input, each of 
# 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# 	which can be "active", “inactive", or "pending". Write an if statement to print 
# 	and "None active" if neither is "active".
status_one =input("Enter from the words 'active,inactive or pending'")
status2 =input("Enter from the words 'active,inactive or pending'")
if status_one =="active" and status2 =="active":
      print("Both active")
elif status_one in ["active","inactive"]
#  11. 	Given a string `filename` supplied by the user, write an if statement to check if the
# 	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	print "Not an image file".

#  12. 	You have a variable `access_level` provided through user input which can be "admin",
# 	"user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	"admin", "Limited access" if it is "user", and "No access" if it is "guest".

mode= input("Are you a guest,admin or user?: ").lower().strip()
if mode =="admin" :
       print("Full access")
elif mode =="user" :
       print("Limited access")
elif mode =="guest":
       print("No access")
else:
       print("Invalid mode")

#  13. 	Given a string `email` collected from the user, write an if statement to check if the
# 	email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
	# print "Invalid email".
email= input("What is your email?(ensure it has symbol '@' and  '.')")

if '@' in email and '.' in email:
       print("The email is valid")
else:
       print("The email is invalid,kindly check again")

#  14. 	You have a variable `day` provided by user input which can be any day of the week 
# 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

day =input("Enter any day of the week: ").lower().strip()
if day in ['Monday','Tuesday','Wednesday','Thursday','Friday'].lower():
     print(f"{day} is a Weekday")
elif  day in ['Saturday', 'Sunday']:
     print(f"{day} is a Weekend")
elif not day in ['Monday','Tuesday','Wednesday','Thursday','Friday'] or not day in ['Saturday', 'Sunday'] :
     print("Enter a valid day")

#  15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# 	input from the user and prints the greatest number. Use conditional statements
# 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# 	statements."Enter a number : ")

number1 =int(input("Enter a number : "))
number2 =int(input ("Enter another number : "))
number3 =int(input("Enter yet another number : "))

if number1 > number2 and number1 > number3:
    print(f"{number1} is greater than {number2} and {number3}")
elif number2 > number1 and number2 > number3:
      print(f"{number2} is greater than {number1} and {number3}")
elif number3 > number1 and number3 > number2:
      print(f"{number3} is greater than {number1} and {number2}")
elif number1== number2 == number3:
     print("The three numbers are equal")