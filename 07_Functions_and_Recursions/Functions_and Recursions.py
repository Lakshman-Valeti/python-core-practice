# Functions and Dictionaries
 # Functions
 # A function is a reusable block of code.
# Function syntax 
def function_name():
    #code
    print()
# Example:
def say_hi():
    print("Hi")

say_hi()    # Calling a function say_hi()     
say_hi()

# Parameters and Arguments 
# Parameters - Variables inside function.
#def greet(name):
#    print("Hello", name)  # Here name is a parameter.
# Arguments - The actual value passed.
#def greet(name):
#    print("Hello", name)
#greet("Lakshman")  # Here Lakshman is an argument.
def greet(name):
    print("Hello", name)
greet("Lakshman")
#greet() # Type error occurs due to missing of argument.

# Multiple Parameters
def addition(a,b):
    print (a + b)
addition(10,20)

# Return statement
# Functions should retuen the statement instead of printing them
def add(a,b):
    return (a+b)
result = add(30,40) # returns value (not print)
print(result)
result_1 = addition(20,30) # In addition() function we already printed the statement in the function so here 50 will be printed.
print(result_1) # None

# Default Arguments
def greet(name="Guest"):
    print("Hello", name)

greet() # If no argument is given, it takes default argument.
greet("Lakshman")

# Keyword Arguments
# we assign Arguments to a value properly, to avoid confusions.
# Order does not matter in keyword arguments.
def student(name, age):
    print(name, age) # Functions prints variables according to this order

student(age=20, name="Lakshman") 

# Positional arguments
# We just give values , function take them according to their position and assigns them to arguments in that position.
# Order matters in positional arguments
def student(name, age):
    print(f"Name:{name} , Age:{age}")

student("Lakshman", 20)
student(20,"Lakshman") # Here 20 is assigned to name and Lakshman is assigned to age

# Examples
def greets(arg_1="Hello",arg_2="Lakshman"):
    print(arg_1+" "+ arg_2)
greeting = input("Enter greeting : ")
name = input("Enter name: ")
greets(arg_2=name) # default value is taken as arg_1 and input name is taken for arg_2.


"""
def greet_1(arg_1="Hi",arg_2): # default argument after keyword argument(gives us a syntax error)
    print(arg_1 + " " + arg_2)
greeting = input("Enter : ")
name = input("Enter name : ")
greet_1(arg_2=name)
"""
def greet_1(arg_2,arg_1="Hi"): 
    print(arg_1 + " " + arg_2)
greeting = input("Enter : ")
name = input("Enter name : ")
greet_1(arg_2=name)

# Passing immutable objects
def increment(a):
    a += 1
    return a

a = 5
increment(a) 
print(a) # 5, cause changing variable ionside function does not effect the value of outside variable.

# Arbitary Arguments 
# Used when number of arguments are unknown .
def total(*args):
    print(args)

total(10,20,30)


def total(*args):
    return sum(args)

print(total(10,20,30))

# Arbitary Keyword arguments
# Used when we don't know how many named arguments might pass in function.
def details(**kwargs):
    print(kwargs)

details(name="Lakshman",age="17")

# Nested Functions
def outer():

    def inner():
        print("Inner")

    inner()

outer()

# Lamda functions
# One line functions
# Normal:
def square(x):
    return x*x
# lamda:
square = lambda x: x*x

print(square(5))
print(square(10))