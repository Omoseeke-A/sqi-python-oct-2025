# # Print numbers from 1 to 5
# # Expected Output:
# # 1
# # 2
# # 3
# # 4
# # 5

i=1
while i<=5:
    print(i)
    i+=1

# # Print "Hello" 3 times
# # Expected Output:
# # Hello
# # Hello
# # Hello

i=1
while i<=3:
    print("Hello")
    i+=1

# # Print only even numbers from 2 to 10 (do not use += 2)
# # Expected Output:
# # 2
# # 4
# # 6
# # 8
# # 10
i=2
while i<=10:
    if i%2==0:
        print(i)
    i+=2

# # Print numbers in reverse from 5 to 1 using a while loop.
# # Expected Output:
# # 5
# # 4
# # 3
# # 2
# # 1

i=int(input ("Enter a number: "))
while i>=1:
    print(i)
    i-=1
# # 5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# # Expected Output:
# # 1
# # 2
# # 3
# # 4
# # 6
# # 7
# # 8
# # 9
# # 10

i=3
numbers=[]
while i<=10:  
  i+=1
  if i==5:
     i+=1
  numbers.append(i)
  
print(numbers)

# #  6. 	Print a square of stars
# # Ask the user to enter a number
# # Example 1:
# # Input: 3

# # Output:
# # ***
# # ***
# # ***



# # Example 2:
# # Input: 5

# # Output:
# # *****
# # *****
# # *****
# # *****

length= int(input("Enter a length: "))
i=0
while i < length:
    print("*" * length)
    i += 1

# # # *****  7.	Print a right triangle of stars
# # Ask the user to enter a number
# # Example:
# # Input: 4

# # Output:
# # *
# # **
# # ***
# # ****

length= int(input("Enter a length: "))
i=0
while i < length:
    print("*"*i)
    i+=1

#     #  8. 	Print a countdown
# # Ask the user to enter a number where they want to start the countdown from.
# # Example:
# # Input: 5

# # Output:
# # 5
# # 4
# # 3
# # 2
# # 1
# # Go!

i=int(input ("Enter a number: "))
while i>=1:
    print(i)
    i-=1
    if i<1:
        print("Go!")
# #  9. 	Print "1" ten times on the same line using a while loop
# # Expected Output:
# # 1111111111

num=1
i=0
number=[]
while i < 10:
    number.append(str(num))
    i+=1
print("".join(number))
    
# 10.  Print a list of the first 12 multiples of 3 starting from 3
i=1
while i< 13:
    lister=lister.append(3*i)
    i+=1
print(lister)


# 12567
# Write a program that uses a while loop to print numbers from 1 to 10.
i=1
while i<=10:
    print(i)
    i+=1

# # Write a program that takes an integer n from the user and calculates the sum of all 
# # natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).

n= int(input("Enter the number: "))
total=0
i = 1
number=[]
while i <= n:
    total+=i
    number.append(str(i))
    i+=1
print(total)
print(f"{i} +{i}")
print(number)
print("+".join(number) + "=" + str(total))
# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
i=int(input ("Enter a number: "))
while i>=0:
    print(i)
    i-=1
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
number = int(input ("Enter a number: "))
i=1
while i<=number:
    if i%2==0:
        i+=1
print(i)
     
    # else:
    #     print("no even number")

# Write a program that takes two integers, base and exponent,
#  from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2 
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625

base_num= int(input("Enter a number as a base: "))

exponent_num= int(input("Enter another number as an exponent : "))

if base_num >0 and exponent_num > 0:
    print(f"{base_num} raised to the power of {exponent_num} is {base_num ** exponent_num}")
else:
    print("Nothng to show")