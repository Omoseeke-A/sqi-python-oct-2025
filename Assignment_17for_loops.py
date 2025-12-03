#  Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)
# number= int(input("Enter an integer: "))

# for total in number:
#     print(total)
#     total+=number

# Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7
# Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60

# numbers = int(input("Enter a number : "))
# for i in range(1,13):
#     print(f"{numbers} x {i} = {numbers * i}")

# Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"

# word = input("Enter a/some word(s) : ")
# for j in range(len(word) ):
#     print(word[-j])
#     if abs(j)== len(word)-1:
#         break

# Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]
# 6.	Write a program that takes an integer input n from the user and prints the first 
# 	n numbers in the Fibonacci sequence. Example:
# 	Input: 10
# 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# n= int(input (" Enter an integer : "))
# i=0
# while i < n:
#     print(i + 1)
#     i+=i
    # if i == n:
    #     break

# number = input(" Enter a number : ")
# a,b =0, 1
# for i in number:
#     i_intt = int(i)
#     print(a)
#     b= b  not done

#  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a 
# 	loop to find and print the largest number in the list. Don’t use the built-in max 
# 	function or anything similar.
# 	Input: "10, 20, 5, 15"
# 	Output: 20

# num = input("Enter numbers separatd by commas : ")
# num_list = [int(nu)]
# print = (int(num_list))
# largest_num = num_list[0]

# for number in num_list:
#     if num> largest_num:
#         largest_num = num
# print(largest_num)
#  8. 	Write a program that takes an integer n from the user and calculates the sum of all 
# 	even numbers from 1 to n. Print the sum.
# 	Input: 10
# 	Output: 30 (2 + 4 + 6 + 8 + 10)

num = int(input("Enter s number : "))
sum_total = 0
even_number = []
for n in range(1, num+1):
    if n % 2 == 0:
        sum_total+=n
        even_number.append(str(n))
        print(f"sum_total {sum_total}" , "+" .join(even_number))
#  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# 	in the string. Print each character along with its frequency. Example:
# 	Input: "hello"
# 	Output:
# h: 1
# e: 1
# l: 2
# o: 1

word = input("Enter a word : ")
occurence = {}
for letter in word:
    if letter in occurence:
        occurence[letter] +=1
    else:
        occurence[letter]=1
for letter,count in occurence.items():
    print(f"{letter} : {count}")
# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# 	squares of all numbers from 1 to n. Print the sum. Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

num = int(input("Enter a number : "))
square_sum = 0
numbers = ""
for i in range(1, num + 1):
    square_sum +=i**2
    if i < num:
        numbers += f"{i}^2 +"
    else:
        numbers +=f"{i}^2 "
print(f"{square_sum} ({numbers})")
#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# 	letter of each word. Print the acronym. Example:
# 	Input: "Portable Network Graphics"
# 	Output: "PNG"

word = input("enter a phrase: ").title()
words = word.split()
shortened= ""
 
for worded in words:
    shortened += word[0]
print(shortened)

#  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# 	Print the count. Example:
# 	Input: "Hello world from Python"
# 	Output: 4

phrase = input("Enter a phrase: ")
words = phrase.split()
count_of_words = 0
for word in words:
    count_of_words += 1
print(count_of_words)


#  13. 	Collect a string from the user and only print put the words that start with the letter 
# 	‘S’. Example:
# 	Input: “Print only the words that start with s in this sentence”
# 	Output: 
# 	start
# 	s
# 	Sentence

sentence = input("Enter a sentence: ").lower()
letter_starwith_s = sentence.split()
for word in letter_starwith_s:
    if word.startswith("s"):
        print(word)

#  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.
#  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# 	by 3.
number = []
for i in range (1,51):
    if i % 3 ==0:
        number.append(i)
    continue
print(number)

# 16.	Go through the string below and if the length of a word is even, print that word.
# 	st = ‘Print every word in this sentence that has an even number of letters’
# 	Output: 
# 	word
# 	in
# 	this
# 	sentence
# 	that
# 	an
# 	even
# 	number
# 	of
sentence = input("Enter a sentence :")
even_words=[]
for word in sentence:
    if len(word) % 2 ==0:
        even_words.append(word)
    continue
print(str(even_words))
print()
#  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# 	are multiples of both three and five, print “FizzBuzz”.

number = range(1,101)
for i in number:
    print(i)
    if i % 3 == 0 and i %5 ==0:
        print("FizzBuzz")
    if i % 3 == 0:
        print("Fizz")    
    if i % 5 == 0:
        print("Buzz")

#  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B


names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
grades = ['A', 'E', 'F', 'C', 'B']

print(list(zip(names, grades)))

for  (names, grades) in zip(names, grades):
    print(f" {names} got grade {grades}")

#  19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

items = ['shoe', 'stick', 'toy', 'fruit']
for i in range(len(items)):
    if i % 2 == 0:
        print(items[i])
    if i==items[2]:
        break

    print()
    print()
    


#  20.	Given two lists of numbers of the same length, print the indices and values
#  	of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
#   'Index 1: 8 != 3',
#   'Index 3: 7 != 9',
#   'Index 5: 4 != 0',
# ]


list1 = [5, 8, 6, 7, 12, 4]
list2 = [5, 3, 6, 9, 12, 0]

for i in range(len(list1)) and range(len(list2) ):

    if list1[i] != list2[i]:
        print(f"At index{i} {list1[i]} is not equal to {list2[i]}")
    else:
        continue
