# -----------------------------------------ASSIGNMENT-----------------------------------------------
# 1. Create a class called Book with the following attributes:
#    - title
#    - author
#    - genre
#    - page_count
#    - year_published
#
#    The class should have a method called short_description() that returns:
#    "{title} by {author} ({year_published}), {genre}, {page_count} pages."
#
#    After defining the class, create 3 different Book objects with different values.
# ---------------------------------------------------------------------------------------------------

class Book:
    def __init__(self,title:str,author:str,year_published:str,genre:str,page_count:int,):
        self.title= title
        self.author =author
        self.genre = genre
        self.page_count = page_count
        self.year_published = year_published
    def short_description(self):
        print(f"{self.title} by {self.author} ({self.year_published}),{self.genre},{self.page_count} pages.")

book1 = Book("Winni winni loju orogun","Omidan 'moseeke","aka takiti",1_054,1954)
book2 = Book("Jesus na umu okoro ya igbo(Jesu and his igbo boys)","Chioma Jesus","954 AD","Oziọma",295)
book3 = Book("Finding Life's Purpose","Myles Nnamdi","2025","Motivational",60)
print()
book1.short_description()
book2.short_description()
book3.short_description()
# -----------------------------------------ASSIGNMENT-----------------------------------------------
# 2. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.

class Car:
     def __init__(self,brand:str,model:str,year:str,horsepower:int,fuel_type:str):
         self.brand = brand
         self.model = model
         self.year = year
         self.horsepower = horsepower 
         self.fuel_type = fuel_type
         
     def car_info(self):
        print (f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}.")
car_1 = Car("Toyota","Camry",2021,203,"Petrol")    
car_2 = Car("Honda","Hybrid",2022,212,"Hybrid")    
car_3 = Car("Tesla","Model 3 Long Range",2023,333,"Electric")    

print()
car_1.car_info()
car_2.car_info()
car_3.car_info()

# 3. Create a class called Student with the following attributes:
#    - name
#    - age
#    - grades (a list of integers)
#
#    The class should have two methods:
#    - average_grade(): returns the average of all grades
#    - is_passing(): returns True if the average grade is >= 50, otherwise False
#
#    After defining the class, create 2 different Student objects with different values.

# Example usage:
# s1 = Student("Alice", 20, [60, 75, 80, 90])
# s2 = Student("Bob", 19, [30, 40, 20, 45])

# print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# Expected Output:
# Alice average: 76.25 passing: True
# Bob average: 33.75 passing: False
class Student:
    def __init__(self,name:str,age:int,grades:list):
        self.name = name
        self.age = age
        self.grades = grades
      
    def average_grade(self):
        return self.name ,"average" ,sum(self.grades)/len(self.grades)

    def is_passing(self):
        average_score = sum(self.grades)/len(self.grades)
        if average_score >= 50:
            return f"Passing : True"
        else:   
           return f"Passing: False"
        
   
student_1= Student("Chinasa",12,[2,30,4])
   
student_2= Student("Chidubem",10,[80,50,50])
print()

# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())
print(student_1.name,"average : ",student_1.average_grade(),"passing:", student_1.is_passing())
# print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())
print(student_2.name,"average : ",student_2.average_grade(),"passing:", student_2.is_passing())
print()

# 4. Create a class called Playlist with the following attributes:
#    - name
#    - songs (a list of strings)
#    The class should have three methods:
#    - add_song(song): adds a new song title to the playlist
#    - total_songs(): returns the total number of songs
#    - show_songs(): returns all song titles as a comma-separated string
#
#    After defining the class, create a Playlist and add a few songs.

# Example usage:
# pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# pl.add_song("Lose Yourself")
# pl.add_song("Can't Hold Us")

# print(pl.name, "has", pl.total_songs(), "songs")
# print("Songs:", pl.show_songs())

# Expected Output:
# Workout Jams has 4 songs
# Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us

class Playlist:
    def __init__(self,name:str,songs:list):
        self.name = name 
        self.songs = songs
       

    
    def add_song(self,song):
        self.songs.append(song)
        print(self.songs)

    def total_songs(self):
      return  len(self.songs)
        
    def show_songs(self):
        return ",".join(self.songs)

pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
pl.add_song("Lose Yourself")
pl.add_song("Can't Hold Us")
pl_2 = Playlist("Spirituals", ["Agbara", "Let the Spirit of Knowing"])
pl_3 =  Playlist("Relax", ["Dance With My Father", "Iye","Sweet Mother","I will be there"])

print(pl.name, "has", pl.total_songs(), "songs")
print("Songs:", pl.show_songs())

print()

print(pl_2.name, "has", pl_2.total_songs(), "songs")
print("Songs:", pl_2.show_songs())

print()

print(pl_3.name, "has", pl_3.total_songs(), "songs")
print("Songs:", pl_3.show_songs())
print()

# 5. Create a class called ShoppingCart with the following attributes:
#    - owner
#    - items (a dictionary where keys are item names and values are prices)
#c
#    The class should have three methods:
#    - add_item(item, price): adds the item with its price
#    - total_cost(): returns the sum of all prices
#    - most_expensive(): returns the item with the highest price
#
#    After defining the class, create a ShoppingCart and add multiple items.

# Example usage:
# cart = ShoppingCart("Alice", {})
# cart.add_item("Laptop", 1200)
# cart.add_item("Mouse", 25)
# cart.add_item("Keyboard", 100)
# cart.add_item("Monitor", 300)

# print("Total cost:", cart.total_cost())
# print("Most expensive item:", cart.most_expensive())

# Expected Output:
# Total cost: 1625
# Most expensive item: Laptop
# ---------------------------------------------------------------------------------------------------

class ShoppingCart:
    def __init__(self,owner:str,items:dict):
        self.owner = owner
        self.items = items
    def add_item(self,item:str,price:int):
        self.items[item] = price
        return self.items
    def total_cost(self):
        return sum(self.items.values())
        
    def most_expensive(self):
        return  max(self.items,key = self.items.get)
        
    
cart = ShoppingCart("Alice", {})
cart.add_item("Laptop", 1200)
cart.add_item("Mouse", 25)
cart.add_item("Keyboard", 100)
cart.add_item("Monitor", 300)
cart.add_item("Donkey", 3000)
cart.add_item("McVities", 5000)
cart.add_item("Food", 30000)

print("Total cost:", cart.total_cost())
print("Most expensive item:", cart.most_expensive())