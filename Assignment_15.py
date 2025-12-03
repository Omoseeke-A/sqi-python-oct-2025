# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.
#
# Example input/output executions:
#
# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed
#
# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed


height = int(input("What is your height in centimeters"))
adult= input(" Are you with an adult?").lower()
if height <120:
    if adult == "yes":
        print("Allowed")
    else: 
        print("Not allowed")
elif height >= 120:
     if adult == "yes" or adult == "no":
        print("Allowed")
   
   # Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".
#
# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail
score = int(input("Enter your score :"))
retake = input("Will you retake the course ? : ").lower()
if score >= 50:
     if retake == "yes" or retake == "no":
        print("Passed")
elif score < 50 :
    if retake =="yes":
        print("Retake allowed")
    else:
        print("Fail")


# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".
#
# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Trip denied
# Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# 800 < 1000 (less than half), so "Trip denied".
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
# Reasoning: cost = 2000; balance = 2000.
# balance >= cost, so "Trip confirmed".
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Add funds
# Reasoning: cost = 2000; half = 1000; balance = 1000.
# not enough (1000 < 2000) but balance >= half, so "Add funds".
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
# Reasoning: cost = 2000; half = 1000; balance = 400.
# balance < half, so "Trip denied".
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Add funds
# Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# not enough (500 < 1000) but exactly half, so "Add funds"

distance = int(input("How many kilometers are you covering? ; "))
wallet =int(input("How much dey your wallet? ; "))

tfare= distance * 200

if distance < 0:
    print(" You cannot have a negative distance ")
elif tfare <= wallet :
    print("Trip confirmed")
elif (wallet < tfare) and (wallet >=(tfare/2)):
    print("Add funds")
elif wallet < (tfare/2):
    print("Trip denied")

# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".
#

# Example input/output executions:
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass
#
# Boarding pass? yes
# Passport? no
# Output: No passport
#
# Boarding pass? no
# Passport? no
# Output: Denied entry
#
# Boarding pass? yes
# Passport? yes
# Output: Proceed to boarding
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass

b_pass = input("Boarding pass?(enter either yes or no) : ").lower().strip()
passport = input("Passport (enter either yes or no)? : ").lower().strip()

if b_pass=="yes" and passport== "yes":
    print("Proceed to boarding")
elif b_pass=="" and passport =="yes" or passport =="no":
    print("No boarding pass")
elif passport=="" and b_pass =="yes" or passport =="no":
    print("No passport")
elif passport=="" and b_pass =="":
    print("Entry Denied")