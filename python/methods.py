#Methods
#Method is a bunch of code that is intended to perform a particular task in your Python’s code.

 #   Function that belongs to a class is called an Method.
 #   All methods require ‘self’ parameter. If you have coded in other OOP language you can think of ‘self’ as the ‘this’ keyword which is used for the current object. It unhides the current instance variable.’self’ mostly work like ‘this’.
 #   ‘def’ keyword is used to create a new method.
 
 
class Vector2D:
        x = 0.0
        y = 0.0
  
        # Creating a method named Set
        def Set(self, x, y):     
                self.x = x
                self.y = y
                
def Main():
        vec = Vector2D()
        vec.Set(5,6)
        print(str(vec.x) + str(vec.y))
        
if __name__=='__main__':
        Main()
        
        
               
        
                
