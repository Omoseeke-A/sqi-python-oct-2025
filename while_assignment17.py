# Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)


# n= input("Enter an integer: ")
# total=0
# i = 0
# number=[]
# while i< int(len(n)):
#     total+=int(n[i])
#     number+=n[i]
#     i+=1
# print(f"{total} is the total of " + "+" .join(number))


# n= input("Enter an integer: ")
# total=0
# i = 0
# number=[]
# for i in range(len(n)):
#     total+=int(n[i])
#     number+=n[i]
# print(f"{total} is the total of " + "+" .join(number))


# Collect a string from the user and use loops to count the number of vowels and consonants in the string. 
# Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7
 
# vowel_store =0
# consonant_store = 0
# word = input("Enter a word or words : ").lower()
# i=0
# j = 0
# while i< len (word) and j < len(word):
#     if word[i] in "aeiou":
#         vowel_store+=1
#     i+=1
#     if word[j] in "bcdfghjklmnpqrstvwxyz":
#         consonant_store +=1
#     j+=1
# print("Cononant:",consonant_store)
# print("Vowel" ,vowel_store)

# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# numbers = int(input("Enter a number : "))
# i = 1
# while i <=12:
#     print(f"{numbers} x {i} = {numbers * i}")
#     i+=1
    
# numbers = int(input("Enter a number : "))
# for i in range(1,13):
#     print(f"{numbers} x {i} = {numbers * i}")
    
    
# Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# word = input("Enter a/some word(s) : ")
# j =-1
# while len(word) >1:
#     print(word[j])
#     j-=1
#     if abs(j)== len(word)+1:
#         break

# word = input("Enter a/some word(s) : ")
# for j in range(len(word) ):
#     print(word[-j])
#     if abs(j)== len(word)-1:
#         break
# Write a program that takes a list of numbers (entered as comma-separated values) 
# from the user and removes any duplicate values.
#  Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]


numbers = input("Enter series of numbers : ").split(",")
number_lister = []

for char in numbers:
    num = int(char)
    if num not in number_lister:
        number_lister.append(num)
print(number_lister)