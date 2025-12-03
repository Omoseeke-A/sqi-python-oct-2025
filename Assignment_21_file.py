# ----------------------ASSIGNMENT---------------------
with open("sample.txt","w")as sample:
    sample.write("""The room was quiet except for the soft hum of a ceiling fan,
stirring the warm evening air. Sunlight slipped through the curtains
in thin, golden lines, casting gentle patterns across the floor. 
""")

# # -------------------------------------------------
# # EXERCISE 1:
# # Open the file "sample.txt" in read mode.
# # Print out the entire file contents.
with open("sample.txt","r") as s:
    content = s.read()
print(content)
print()

# # ----------------------------------------------------------

print("2.")# # EXERCISE 2:
# # Open "sample.txt" again, but this time print only the first line.
with open("sample.txt","r") as s:
   one_line = s.readline() 
   print(one_line)
# # ----------------------------------------------------------

# # EXERCISE 3:
# # Read all the lines in "sample.txt" into a list called lines.
# # Then print the last line in the file.

print("3.")
with open("sample.txt","r") as s:
   lines = s.readlines() 
   print(lines[-1])
    
# # ----------------------------------------------------------
print("4.")
# # EXERCISE 4:
# # Create a new file called "notes.txt" using write mode.
# # Write three lines into it (each ending with a newline):
# #   - "Python file test"
# #   - "We are learning to write files"
# #   - "This is the third line"
with open("notes.txt","w") as n:
  n.write(f"Python file test.'\n' We are learning to write files.\n-This is the third line.\n")  
  print()
    
# # ----------------------------------------------------------
print("5.")
# # EXERCISE 5:
# # Open "notes.txt" again in append mode.
# # Add one more line that says:
# #   "This line was appended."
with open("notes.txt","a") as n:
  n.write("This line was appended")  
  print()
# # # ----------------------------------------------------------

print("6.")
# EXERCISE 6:
# # Open "notes.txt" again in read mode.
# # Print all its contents to confirm the new line was appended.
with open("notes.txt","r") as n:
   notes = n.readlines() 
   print(notes)
   print()
# # # ----------------------------------------------------------
print("7.")
# # EXERCISE 7:
# # Read all lines from "sample.txt".
# # Using a for loop with enumerate, print each line like this:
# #   Line 1: <the line>
# #   Line 2: <the line>
# # Strip out the newline characters when printing.
with open("sample.txt", "r") as sample:
   for s in enumerate(sample, start = 1):
      # rem = s.replace('\n','')
      print(s)
# # ----------------------------------------------------------
print("8.")
# # EXERCISE 8:
# # Do the same as Exercise 7, but using a while loop instead of for loop.
while s < sample:
   print(s)
   s+=1
    
# # ----------------------------------------------------------
print("9.")
# # EXERCISE 9:
# # Open "notes.txt" in read mode.
# # Count how many lines are in the file and print:
# #   "notes.txt has X lines"
count = 0
with open("notes.txt","r") as notes:
   for n in notes:
      count +=1
   print(f"notes.txt has {count} lines")
# ----------------------ASSIGNMENT---------------------