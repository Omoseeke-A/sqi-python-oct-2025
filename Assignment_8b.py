num1=15
num2=4
print(f"Normal division between {num1} and {num2} is {num1 / num2}")
print(f"Float division between {num1} and {num2} is {num1 // num2}")
print(f"The remainder between 20 and 6 is {num1 % num2}")

# BALLS AND BOXES
apples = 95
boxes = 8

print(f"The number of apples in each box will be {apples // boxes}")
print(f"The number of apples remaining will be {apples % boxes}")

minutes=505
print(f"{minutes} minutes is {minutes // 60} hours, {minutes % 60} minutes.")

# EVEN NUMBER CHECK
NUM= int(input("Enter a number : "))
is_even =NUM%2==0
print(is_even)

# MULTIPLE OF 3
multiple_3= int(input("Enter a multiple of 3: "))
is_multiple = multiple_3 % 3==0
print(is_multiple)

# REMAINDER EXERCISE

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

print(f" The remainder of {num1} and {num2} is {num1 % num2}")

#HOURS AND MINUTES CONVERTER

minutes= int(input("Enter a value in minutes"))
print(f"{minutes} minutes is {minutes // 60} hours, {minutes % 60} minutes.")

# OBJECT DISTRIBUTION
candies = int(input("How many candies are to be shared? : "))
children = int(input("How many children are to share the candies? :"))

print(f"Each child will have {candies // children} with {candies % children} remaining")

# MULTIPLE OF 10
multiple_10= int(input("Enter a  number to check if it is a multiple of 10: "))
is_multiple = multiple_10 % 10==0
print(is_multiple)