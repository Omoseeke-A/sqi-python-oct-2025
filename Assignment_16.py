
# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. 
# E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, 
# their guess is too low.
# import random
# random_num = random.randint(1,50)
# # print(random_num)
# i=0
# guess_num = int(input(" Guess a number : "))
# while True:
#     if guess_num!=random_num:
#         if i<5:
#             print("Take another guess :")
#             i+=1
#      else: ("Trials exhausted")
# print("You got it")
# break

# Write a program that keeps asking the user for a password until they enter the correct one. 
# The correct password is `secret`.
while True:
    password = input("Enter the correct password: ")
    if password == "secret":
        print("Password correct!")
        break
    else:
        print("Wrong,try again")
# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
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
# Write a program that takes a string input from the user and uses a while loop to count the number of vowels (a, e, i, o, u) in the string.
# Write a program that takes a string input from the user and uses a while loop to reverse the string.
# Do not use slicing or reversed().
#  10.	Write a program that takes comma-separated integers from the user, converts that
# 	to a tuple and uses a while loop to find the minimum value in the tuple. Do not 
#       Use the min() function.
#  11. 	Write a program that takes a string input from the user and uses a while loop to count
# 	the occurrences of each character, storing the counts in a dictionary.
# 	Sample Input:
# 	Enter a string: Hello
# 	Sample Output:
# 	{‘h’: 1, ‘e’: 1, ‘l’: 2, ‘o’: 1}