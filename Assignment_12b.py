# Create a dictionary called `student` with keys "name", "age", and "grade", and 
# corresponding values "John", 20, and "A". Access and print the value of "name".

student={"name":"John" ,"age":20 ,"grade" : "A"}
print(student)
# Create a dictionary called `product` with keys "name", "price", and "stock", and 
# corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
product={"name":"Laptop","price":999.99, "stock": 50}
print(product)
product["price"]=899.99
print(product)
# Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager".
#  Add a new key "salary" with the value 50000.
employee={"name":"Alice","position":"Manager"}
employee.update({"salary":50000})
# Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively.
#  Remove the key "banana".
inventory= {"apple":10, "banana":5,  "orange":8}
print(inventory)
inventory.pop("banana")
print(inventory)
# Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York".
#  Use the copy() method to make a copy of the dictionary and call it person_copy.
person={"name":"Bob" ,"age":25 ,"city" : "New York"}
print(person)
person_copy=person.copy()
print(person_copy)

# Create a nested dictionary called `family` with keys "child1", "child2", and "child3",
#  each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
family = {
"child1":{"name":"Ken","age":2},
"child2":{"name":"Kenny","age":20},
"child3":{"name":"Kenne","age":23}
}
print(family)

# Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020.
#  Access and print the value of "model".

car= {"brand":"Toyota","model":'Corolla' ,"year":2020}
print(car.get("model"))
# Create a dictionary called `settings` with keys "volume", "brightness", and "language",
#  and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings={"volume":50,"brightness":75,"language":"English"}
print(settings)
settings["language"]="Spanish"
print(settings)
# Create a dictionary called `scores` with keys "math", "science", and "english", 
# and corresponding values 90, 85, and 88. Remove the key "science"

scores={"math":50,"science":85,"English":88}
print(scores)
scores.pop("science")
print(scores)
# Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", 
# and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
menu= { "starter":"soup","main_course": "steak", "dessert": "ice cream"}
print( "appetizer" in menu)
# Create a dictionary called `config` with keys "theme", "language", and "timezone",
#  and corresponding values "dark", "English", and "UTC". Clear the dictionary.

config={"theme":"dark","language":"English", "timezone":"UTC"}
print(config)
config.clear()
print(config)

#  12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and 
# "Charlie", and corresponding phone numbers as values. Print the number of 
# items in the dictionary.
phonebook={"Alice":23456,"Bob":67891,"Charlie":12345}
print(len(phonebook))
#  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
grades= {"math": "A","science":"B","history":"C"}
print(grades.keys())
#  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# of all the values in the dictionary.
employee={"name":"David","position":"Engineer","salary":70000}
print(employee.values())
#  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# key-value pairs in the dictionary.
game={"title":"Minecraft","genre":"Sandbox","rating":4.5}
print(game.items())
