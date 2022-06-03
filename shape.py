# Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr






import math




class Circle:
    def __init__(self,radius):
     self.radius=radius
     
     
    def area(self): 
      A=math.pi*self.radius**2
      return A
     
      
    def circumference(self): 
         #C=2πr
      C= 2 * math.pi * self.radius 
      return C
    
    
    
# Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a

class Square:
    def __init__(self,side):
        self.side=side
        
    def area(self):
        A=self.side*self.side
        
        return A  
    
    def perimeter(self):
        P=4*self.side
        return P    
    
    
# Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) of the rectangle using the formula P=2(l+w)
     
class Rectangle:
    def __init__(self,w,l):
        self.width = w
        self.length = l
       
         
        
    def area(self):
        A=self.width*self.length
        return A
        
    def  perimeter(self):
        P=2(self.width+self.length)  
        return P     
        
    
# Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) of the sphere using the formula V = 4/3(πr3)

class Sphere:
    def __init__(self,r):
        self.r=r
        
    def area(self):
        A=4*math.pi**2   
        return A 
    
    def volume(self):
        V= 4/3*math.pi**3
        return V
    
    


    
