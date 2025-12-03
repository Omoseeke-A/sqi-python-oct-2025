

import copy

animals=["dog","cat","goat","cow","sheep","horse"]
print(animals[1]+ ", " + animals[-2])

#2
animals[0]=["lion"]
animals[-1]=["elephant"]
print(animals)

# 3
animals.append("pig")
animals.insert(2,"hen")

# 4
animals=["dog","cat","goat","cow","sheep"]
animals.remove("cow")
print(animals)

# 5
print("goat" in animals)

# 6
food1=["rice", "beans"]

food2=["yam", "plantain"]
print(food1 + food2)

# 7
drinks=["tea","coffee","juice"]
print("water" in drinks)

# 8
drinks.extend(["water", "milk"])
print(drinks)

# 9
drinks[1]="hot chocolate"
print(drinks)

# 10
vehicles=["car","bike","bus","train"]
print(vehicles)

# 10a
vehicles.append("boat")
print(vehicles)

# 10b
vehicles.insert(1,"truck")
print(vehicles)

# 10c
vehicles.remove("bike")
print(vehicles)

# 10d
print(vehicles)
print('plane' in vehicles)

# 11
cities=["Lagos","Kano","Ibadan"]
cities.append("Abuja")
print(cities)

# 12
cities=["Lagos","Kano","Ibadan"]
more_cities=["Abuja", "Enugu"]
print(cities + more_cities)
