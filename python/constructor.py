#Syntax of constructor declaration : 

#def __init__(self):
    # body of the constructor

#Types of constructors : 

#    default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. Its definition has only one argument which is a reference to the instance being constructed.
#    parameterized constructor: constructor with parameters is known as parameterized constructor. The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.
 

class sachin:

    #default constructor 

    def __init__(self):
        self.amingad = "London"

    def print_sachin(self):
        print(self.amingad)

#creating object of the class 
obj = sachin()

#calling the instance method 
obj.print_sachin()


