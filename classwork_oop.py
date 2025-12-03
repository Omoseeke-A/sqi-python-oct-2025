class Car:
    def __init__(self,color,brand,model,year_manufactured,engine,no_of_doors):
        self.color = color
        self.brand = brand
        self.model = model
        self.year_manufactured = year_manufactured
        self.engine = engine
        self.no_of_doors = no_of_doors
     
    def move(self):
        return f"{self.brand} has moved"
     
    def reverse(self):
        return f"{self.brand} has reversed"
    def honk(self):
        return f"{self.brand} is honking"
    
mitsubishi = Car("Black","mitsubishi","sagata",2035,"v6",4)
mustang = Car("Grey","Mustang","Mustangushi",2038,"v2",2)
ferarri = Car("Maroon","Ferarri","Kapish",2028,"engine sonata",3)
print(f"Mitsubishi is {mustang.color} in color, and is pf the brand {mustang.brand} and model{mustang.model}. It was manufactured in the year {mustang.year_manufactured}.It also has {mustang.no_of_doors}")

print(mitsubishi.move())
print(mitsubishi.reverse())
print(mitsubishi.honk())


class Movie:
    def __init__(self,title,producer,director,year):
        self.title = title
        self.producer = producer
        self.director = director 
        self.year = year
        
    def change_title(self):
        new_title = input("what is the new title? : ")
        self.title = new_title
        print( f"{self.title}")
    
movie_1 = Movie("Things Fall Apart"," Chinua Achebz","Chinua Achebe",1934)
print(f" The title is {movie_1.title}")
movie_1.change_title()
print(f" The title is {movie_1.title}")
