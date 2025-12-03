# my_favorite_food= ["Yam","Amala with Abula pelu goat meat and ponmo kika"]
# print(my_favorite_food)

sum_of_two_digits= input("Enter two digits")
print(f" The sum of {sum_of_two_digits[0]}" + int(sum_of_two_digits[0])+int(sum_of_two_digits[1]))


#means of transportation
# Create a list called names_of transprt containing the following means of transport:
# car,lorry,camel,ship,canoe

# ADD "PLANE" TO THE END
# ADD JET IN BETWEEN "LORRY" AND "CAMEL"
# CHECK IF "HELICOPTER IS IN THE LIST
# REMOVE "CANOE" FROM THE LIST
# CHANGE LORRY TO VAN
# ADD HELICOPTER AND BROOM AT THE SAME TIME TO TH LIST

names_of_transport=["car","lorry","camel","ship","canoe"]
# 1
names_of_transport.append("Plane")
print(names_of_transport)
# 2
names_of_transport.insert(2,"Jet")
print(names_of_transport)
# 3
print("helicopter" in names_of_transport)

# 4
names_of_transport.remove("canoe")
print(names_of_transport)

# 5
names_of_transport[1]="van"
print(names_of_transport)

# 6
names_of_transport.extend(["helicopter","broom"])
print(names_of_transport)
