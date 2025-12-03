# number = int(input("Enter a number; "))
# if number%2 == 0:
#     print("It is even")
# else:
#     print("It is odd")


# name = input("What is your name?; ")

# listed_name = list(name)
# if listed_name[0] == "A" or listed_name[0]=="a":
#     print("Your name starts with A")
# else :
#     print("Your name does not start with A") 


# score= int(input("Enter your score: "))

# if score < 0:
#     print("There is no negative score")
# elif score==0 or score <=40:
#     print("Your grade is F")
# elif score >=40 and score <=45:
#     print("Your grade is E")
# elif score >=46 and score <=50:
#     print("Your grade is D")
# elif score >=50 and score <=59:
#     print("Your grade is C")
# elif score >=60 and score <=69:
#     print("Your grade is B")
# elif score >=70 and score <=100:
#     print("Your grade is A")
# else:
#     print("Score cannot exceed 100")

# has_raincoat= True
# has_umbrella= True

# if has_raincoat and has_umbrella:
#     print("You have double protection from the rain.")

# elif has_raincoat or has_umbrella:
#     print("You are protected from the rain.")

# else:
#     print("You are not protected from the rain")

mode = input("Enter your preferred mode between options: Automatic,manual or off : ").lower()


if mode == "automatic":
    print("Automatic mode activated")
elif mode == "manual":
    print("Manual mode activated")
elif mode == "off":
    print("System is off")
else:
    print("Choose from the stated option")
