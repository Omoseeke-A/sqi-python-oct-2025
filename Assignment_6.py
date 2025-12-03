names="James John Kennedy"
names_list=names.split(" ")
print(names_list)

# 18

cities_list=['New York', 'Los Angeles', 
'Chicago']
cities_string = "; ".join(cities_list)
print(cities_string)

# 19
sentence="the quick brown fox jumps over the lazy dog"
print(sentence.capitalize())

# 20
book_title="to kill a mockingbird"
print(book_title.title())

# 21
greeting="hello world"
print(greeting.count("o"))

# 22
filename="document.txt"
print(filename.startswith("doc"))

# 23
url="https://www.example.com"
print(url.endswith(".com"))

# 24
phrase="find the needle in the haystack"
print(phrase.find("needle"))

# 25
name="Alice"
land="Wonderland"
print("Hello {} .Welcome to {}." .format(name,land))

# 26
quote="To be or not to be."
print(quote.find("not"))

# 27
word="hello"
print(word.islower())

# 28
shout="HELLO"
print(word.isupper())
 
# 29
mixed_case="PyThOn"
print(mixed_case.lower())

# 30
mixed_case="PyThOn"
print(mixed_case.upper())

# 31
padded_text=" hello "
print(padded_text.lstrip())

# 32
padded_text=" hello "
print(padded_text.rstrip())

# 33
padded_text=" hello "
print(padded_text.strip())

# 34
greeting="Hello,World!"
print(greeting.replace("World","Alice"))

# 35
course_name = "Introduction to Python"
print(course_name[:12])
print(course_name[-6:])