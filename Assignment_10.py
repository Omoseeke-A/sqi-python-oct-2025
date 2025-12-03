# """ Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
fruits=["apple", "banana", "orange"]
print(fruits[0])
# Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
colors= ["red", "green", "blue"]
print(colors[-1])

# Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7 (inclusive of index 3, exclusive of 8).
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[3:8])

# Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
           "q","r","s","t","u","v","w","x","y","z"]
print(alphabets[-3:])
# Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
ages=[20,30,40]
ages[1]=35
print(ages)
# Create a list called grades with items "A", "B", "C", "D". Replace the items from index 1 (inclusive) to index 3 (exclusive) with "X".
grades=["A","B","C","D"]
grades[:3]="X"
print(grades)

# Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
cities=["New York", "London", "Paris"]
cities.insert(0,"Tokyo")
print(cities)
# Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
fruits=["apple", "banana", "cherry"]
print(len(fruits))
# Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
items=[ 10.5, 20.0, 15.75]
print(type(items))
# Create a list called mixed with items 10, "apple", True. Print the list.
mixed=[10, "apple", True]
print(mixed)
# Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
tuple_data=("a", "b", "c")
print(list(tuple_data))
# Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
books=["Python", "Java"]
books.append("Javascript")
print(books)
# Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
names=["Alice", "Bob", "Eve"]
names.insert(1,"Charlie")
print(names)
# Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
list1=[1,2,3]
list2=[4,5,6]
total_list=list1.extend(list2)
print(list1)
# Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
students=["Alice","Bob"]
extra_students=("Charlie","David")
students.extend(extra_students)
print(students)
# Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
colors=["red", "green", "blue"]
colors.pop(1)
print(colors)
# Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
numbers=[10,20,30,40]
del numbers[2]
print(numbers)
#  18.	Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
fruits=[ "apple", "banana", "cherry"]
fruits.clear()
print(fruits)
#  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
names=["Zoe", "Alice", "Bob"]
names.sort()
print(names)
#  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
ages=[25,35,20]
ages.sort(reverse=True)
print(ages)
#  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
words=[ "Apple", "banana", "Orange"]
words.sort(key=str.lower)
print(words)

#  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
numbers=[1, 2, 3, 4]
numbers.reverse()
print(numbers)
#  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# 	slicing.
letters= ["a", "b", "c", "d"]
print(letters[::-1])
#  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
original=["one", "two", "three"]
original_copy= original.copy()
print(original)
print(original_copy)
#  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# 	list2 together.
lists1=["a","b"]
lists2=["c","d"]
print(lists1 + lists2)
#  26.	Access and print the second subject of the first person in the list.
# 	data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]

data = [
	["Alice", 25, ["Math", "Physics"]],
    ["Bob", 30, ["Chemistry", "Biology"]],
    ["Charlie", 35, ["History", "Geography"]]
]
print(data[0][2][1])
#  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# 	records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]

records = [
    ["New York", [10, 20, 30]],
    ["San Francisco", [40, 50, 60]],
    ["Austin", [70, 80, 90]]
]
print(records[1][1][0])
# 28.	Get the first e in Ayo’s gender and Get Ben’s age.
#  	group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
group = [
    ["Ayo", ["Female", 12]],
    ["Ben", ["Male", 9]]
]
print (group[0][1][0][5])
print (group[1][1][1])
#  29.	Get the l in Nina’s gender and Get Tobi’s age
# 	records = [
#     ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]

records = [
["Tobi", ["Male", [6]]],
["Nina", ["Female", [7]]]
]
print (records[1][1][0][4])
print (records[0][1][1])
#  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# robot_grid = [
#     ["R2", ["battery", [98]]],
#     ["R5", ["status", "active"]],
#     ["X1", [["joint", "loose"], "error"]]
# ]

robot_grid = [
    ["R2", ["battery", [98]]],
    ["R5", ["status", "active"]],
    ["X1", [["joint", "loose"], "error"]]
]

print(robot_grid[2][1][0][1][1:3])
print(robot_grid[0][1][1])

#  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# playlist = [
#     ["Jazz", ["Take Five", 5.24]],
#     ["Pop", ["Blinding Lights", 3.20]],
#     ["Rock", ["Bohemian Rhapsody", 5.55]]
# ]

playlist = [
    ["Jazz", ["Take Five", 5.24]],
    ["Pop", ["Blinding Lights", 3.20]],
    ["Rock", ["Bohemian Rhapsody", 5.55]]
]
print(playlist[0][1][0][-4:])
print(playlist[0][1][1])
#  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# animals = [
#     ["Elephant", ["Herbivore"]],
#     ["Tiger", ["Carnivore"]],
#     ["Frog", ["Amphibian"]]
# ]

animals = [
    ["Elephant", ["Herbivore"]],
    ["Tiger", ["Carnivore"]],
    ["Frog", ["Amphibian"]]
]
print(animals[1][1][0][5])
# """


