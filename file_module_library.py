with open("my_story.py","w") as f:
    f.write("""This is my story ,
This is my song,
Praising my Saviour,
                """)
    

with open("my_story.py " , "a") as add:
    add.write("All the day long.")

with open ("my_story.py","r") as s:
   display =  s.read()
print(display)

with open("my_story.py " , "a") as add:
    add.write(" You are marvelous.")

with open ("my_story.py","r") as s:
   display =  s.read()
print(display)