# oject Overview:
# Develop a simple Computer-Based Testing (CBT) program in Python that hardcodes a set of 
# at least 5 objective questions and their answers. The program should ask these questions 
# to the user one by one and display the user's score at the end.

# Requirements:
# Hardcode Questions and Answers:
# Create at least 5 objective questions (multiple choice or true/false).
# Hardcode these questions and their correct answers in your program.
# Question Prompting:
# Prompt the user with each question one by one.
# Allow the user to input their answer for each question.
# Scoring System:
# Compare the user's answers with the correct answers.
# Keep track of the user's score.
# Display Results:
# At the end of the quiz, display the user's total score.

score =0
question = input("1. What is 2 + 2?").lower()
""" a) 3
    b) 4
    c) 5
    d) 6"""
if question == "4" or question == "c":
    score+=1
score+=0
question = input("What color is the sky on a clear day?").lower()
"""
a) Red
b) Blue
c) Green
d) Yellow"""
if question == "blue" or question == "b":
    score+=1
score+=0
question = input("How many legs does a spider have?").lower()
"""a) 6
b) 7
c) 8
d) 9"""
if question == "8" or question == "c":
    score+=1
score+=0
question = input("What sound does a cow make?").lower()
"""a) Meow
b) Bark
c) Moo
d) Quack"""
if question == "moo" or question == "c":
    score+=1
score+=0
question = input("What is the opposite of 'hot'?").lower()
"""a) Warm
b) Cold
c) Cool
d) Boiling"""
if question == "cold" or question == "b":
    score+=1
score+=0

print(f"You scored {score} out of 5")