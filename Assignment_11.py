# # Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# length, width, and height, and print each variable.
dimensions= 10, 20, 30
length,width,height=dimensions
print(length)
print(width)
print(height)

# Given the tuple coordinates:
# coordinates = (1.5, 2.5, 3.5)
# Unpack the tuple into variables x, y, and z, and print the value of y.
coordinates = (1.5, 2.5, 3.5)
x, y, z=coordinates
print(y)
# Create a tuple called person with values ("John", 25, "Engineer").
#  Unpack the values into variables name, age, and profession,and print the value of profession.
person= ("John", 25, "Engineer")
name,age,profession=person
print(profession)

# Given the nested tuple data:
# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# Unpack the first element of data into variables student1 and student2, and print student2.

data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
((student1,student2),(subject1,subject2),(score1,score2))=data

print(f"Student 2 is : {student2}")

# Create a tuple called colors with values ("red", "green", "blue", "yellow"). 
# Unpack the first two values into variables color1 and color2, and print both variables.

colors =("red", "green", "blue", "yellow")
color1,color2,_,_=colors
print(f"Values of color 1 and color 2 are :{color1} and {color2},respectively.")
# Given the tuple record:
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments.
#  Print the extracted age and the first department.
record = ("Jane", (32, "Manager"), ["HR", "Finance"])
(name,(age,pos),(dept1,dept2)) = record
print(f"Age: {age} and Department :{dept1}")


# Create a tuple called triplet with values ("one", "two", "three").
#  Unpack the tuple into variables and print the value of the second variable.
triplet=("one", "two", "three")
fist,second,third =triplet
print(f"Second value from the triplet is : {second}")

# Given the tuple info:
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# Unpack the tuple to get the product ID, category, price, and manufacture date. 
# Print the category and the manufacture year.

info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
(productI_D), (category, price),(month,day,year) = info
print(f"Category is :{category},and year of manufacture is {year}")

# Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). 
# Unpack the nested tuples into individual variables and print the second value of the third tuple.

nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
((oneA,twoB), (threeC,fourD), (fiveE,sixF))= nested_tuple
print(sixF)

# Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.

inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
((fruit1,price1) ,(fruit2,price2) ,(fruit3,price3))=inventory
print(f"Price of {fruit3} is {price2}")