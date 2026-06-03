# Variables and Data Types
#Variables are the containers for stroring values. They are used to store data that can be used and manipulated in a program.

# 1. Storing Text
user_name = "Lakshman" # Here user_name is a variable and "Lakshman" is a string value assigned to it.
print(user_name) # Prints the value of the Variable 

# 2. Storing Numbers 
age = 25 # Here age is a variable ane 25 is a prime number assigned to it.
print(age) # Prints the value of the variable age. 

# 3. storing Decimal Numbers 
pi = 3.14 # Here pi is a variable and 3.14 is the value assigned to it.
print(pi) # Prints the value of the variable pi 

# 4. Storing Boolean Values 
is_student = True # Here is_student is a variable and True is a boolean value assigned to it.
print(is_student) # Prints the value of the variable is_student 

# Data Types 

# 1. String Data Type 
# A String is a sequence of characters enclosed in quotes.
name = "Lakshman" # Here the text Lakshman is enclosed in double quotes, making it a string data type.
print(name)

# 2. Integer Data type 
# An Integer is a whole number without a decimal point.
number = 25 # Here 25 is a integer.
print(number)

# 3. Float Data Type
# A float is a number that has a decimal point.
decimal_number = 7.6 # Here 7.6 is a float data type.
print(decimal_number)

# 4. Boolean Data Type
# A Boolean is a data type that can only have two values: True or False.
is_raining = False # Here False is a Boolean Data Type.
print(is_raining) 

# Lists , Tuples , Sets and Dictionaries are also data types.

# Data type checking 
# We can check the data type of a variable using type() function.
print(type(name)) 
print(type(number))
print(type(decimal_number))
print(type(is_raining))
 
# Data type conversion
# We can convert one data type to another using type conversion functions.
# Converting Integer to Float
float_number = float(number) # Here we are converting the the integer value stored in number to a float using the float() function.
print(float_number)
print(type(float_number))

int_number = int(decimal_number) # Float to Integer
print(int_number)
print(type(int_number))

string_number = str(number) # Integer to String
print(string_number)
print(type(string_number))

boolean_value = bool(number) # Integer to Boolean
print(boolean_value) # Prints True for any non-zero integer and False for zero.
print(type(boolean_value))

#input function
# The input() function is used to take input from the user.
user_input = input("Enter your name: ") # This takes input from the user and stores it.
print(user_input)

age_input = int(input("Enter your age: ")) # Here the input from user is coverted to an integer.
print(age_input)

# String Concatenation
# We can conacatenate strings using the + operator.
sentence = "My name is " + user_input + " and I am " + str(age_input) + " years old." # Here we are concatenating the string with the user input and age input.
print(sentence)

#f-strings
# f-strings are a way to format strings in Python. They allow us to embed expressions inside string literals, using curly braces {}.
f_sentence = f"My name is {user_input} and I am {age_input} years old." 
print(f_sentence)
