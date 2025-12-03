
while True:
    # age = int(input('what is your age ?: '))
    try:
        age = int(input('what is your age ?: '))

    except ValueError:
        print("Enter a number!")
    else:
        if (age < 0):
            print(f"age cannot be negative")
            # continue
    
        print(f"You are {age} years old")
