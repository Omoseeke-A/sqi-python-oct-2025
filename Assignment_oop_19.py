# # Fill in the class

# class Cylinder:
#     def __init__(self, height=1, radius=1):
#         self.PI = 3.142
#         self.height = height
#         self.radius = radius
#     def volume (self):
#         return self.PI *( self.radius**2)* self.height

#     def surface_area(self):
#         return 2 * self.PI * self.radius *  (self.radius + self.height)

# # EXAMPLE EXECUTION

# cylinder = Cylinder(2,3)
# print(cylinder.volume())  # 56.52
# print(cylinder.surface_area())  # 94.2


# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.

import math
class Line:
    def __init__(self, coor1(a,b) ,coor2(y,z)): 
        self.coor1 = coor1
        self.coor2 = coor2
        

    def distance(self,a,b):
        return math.sqrt(self.coor1((b-a)**2) + self.coor2((b-a)**2))

    def slope(self,a,b):
        return (self.coor2(b-a)/self.coor1(b-a))

# EXAMPLE EXECUTION

coordinatel = (3,2)
coordinate2 = (8,10)

line_1 = Line(coordinatel, coordinate2)

print(line_1.distance(a,b))  # 9.433981132056603
print(line_1.slope(a,b))  # 1.6
