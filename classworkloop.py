# # length = int(input("Enter a length: "))
# # i = 0
# # while length>=i:
# #     print("*" * length)
# #     length-=1

# sentence =input("Give me a random sentence :")
# i = 0
# while i < len(sentence):
#     print(sentence[i])
#     i+=1


# musical_instrument=["gong","drum","saxophone","guitar","keyboard"]
# i = 0
# while i < len(musical_instrument):
#     print(f"{i + 1}." + musical_instrument[i])
#     i+=1

while True:
    food=input("Whatt is your favourite food?: ").lower()

    if food.startswith("r"):
        print("Alright!")
        break

    print("Give me a food that starts with r")