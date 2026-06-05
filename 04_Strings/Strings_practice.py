# Strings Practice
# A string is a sequence of characters enclosed in quotes.
# You can use single quotes (' ') or double quotes (" ") to create a string.
# Triple quotes (''' ''' or """ """) can be used for multi-line strings.
# Example of multi-line string:
from pydoc import text


multi_line_string = """My name is Lakshman.
I love programming.
My favorite programming language is Python."""
print(multi_line_string)

# String Indexing
# You can access individual characters in a string using indexing.
# Indexing starts at 0 for the first character.
Text = "Hello World"
# H starts at index 0, e is at index 1, l is at index 2, and so on.
# Space also counts as a character and is at index 5.
print(Text[0])  # Output: H
print(Text[6])  # Output: W
# If we try to access an index that is out of range, we will get index error.
# print(Text[20])  # This will raise an IndexError

# Negative Indexing
# You can also use negative indexing to access characters from the end of the string.
# Last chracter is at index -1, second last is at index -2, and so on.
print(Text[-1])  # Output: d
print(Text[-2])  # Output: l

# String Slicing
# You can extract a substring from a string using slicing.
# The syntax for slicing is: string[start:end:step].
# start is the index where the slice starts (includes the start index).
# end is the index where the slice ends (does not include the end index).
# step is the number of characters to skip (optional).
# Example of slicing:
print(Text[0:5])  # Output: Hello
print(Text[6:11])  # Output: World
# string[:] will give you whole string
print(Text[:])  # Output: Hello World
print(Text[:4]) # Starts from index 0 and ends at index 4 (does not include index 4).
print(Text[6:]) # Starts from index 6 and goes till the end of the string.
# You can also use negative indices in slicing.
print(Text[-5:])  # Output: World
print(Text[:-6])  # Output: Hello

# Strings are immutable.
# This means that you cannot change a string after it has been created.
# If you try to change a character in a string, you will get a TypeError.

# len() function can be used to find the length of a string.
print(len(Text))  # Output: 11

# String Concatenation
# You can concatenate (combine) two or more strings using the + operator.
first_name = "Lakshman"
last_name = "Valeti"
full_name = first_name + " " + last_name
print(full_name)  # Output: Lakshman Valeti

# String Repetition
# You can repeat a string multiple times using the * operator.
message = "Hi"
print(message * 3) # Output: HiHiHi

# Membership operator
# You can check if a substring is present in a string using the in operator.
s = "Python"
print("th" in s)
# You can check if a substring is not present in a string using the not in operator.
print("z" not in s) # Output: True

# String Methods 
name = "LuCkEe"

# 1. upper() - Converts all characters in a string to uppercase.
print(name.upper()) # Output: LUCKEE

#2. lower() - Coverts all characters in a string to lowercase.
print(name.lower()) # Output: luckee

# 3. title() - Converts the first character of each word to uppercase and remaining characters to lowercase.
movie = "the adam project"
print(movie.title()) # Output: The Adam Project

# 4. strip() - Removes leading and trailing whitespaces from a string.
text_s = "   Hello World   "
print(text_s.strip()) # Output: Hello World
# lstrip() - removes whitespaces on left side of the string.
print(text_s.lstrip()) # Output: Hello World
#rstrip() - removes whitespaces on right side of the string.
print(text_s.rstrip()) # Output:   Hello World 

# 5. replace() - Replace a specified substring with another substring.
greeting = "Hello World"
new_greeting = greeting.replace("World", "Python")
print(new_greeting) # Output: Hello Python

# 6. split() - Splits a string into a list of substrings based on a specified delimiter (By default, it splits by space).
sentence = "Python is a great programming language"
words = sentence.split()
print(words) 

# 7. join() - Joins a list of strings into a single string using a specified delimiter.
word_list = ["Python", "is", "awesome"]
joined_string = " ".join(word_list)
print(joined_string) # Output: Python is awesome.
joined_string_comma = ",".join(word_list)
print(joined_string_comma) # Output: Python,is,awesome

# 8. find() - Returns the index of the first occurrence of a specified substring in a string.
# If the substring is not found, it returns -1.
text_h = "Hello World"
find_substring = text_h.find("World")
print(find_substring) # Output: 6
sub_string = text_h.find("Python")
print(sub_string) # Output: -1

# 9. index() - Returns the index of the first ocurrence of a specified substring in a string.
# If the substring is not found, it give error.
text_h = "Hello World"
substring_index = text_h.index("rl") 
print(substring_index) # Output: 8
# substring_index = text_h.index("Python") gives an error

# 10. count() - Returns the number of occurrences of a specified substring in a string.
text_c = "Hello World, Hello Python"
count_hello = text_c.count("Hello")
print(count_hello) # Output: 2
count_python = text_c.count("Python")
print(count_python) # Output: 1

# 11. Capitalize() - Converts the first character of a string to uppercase and the rest to lowercase.
text_cap = "hello world"
capitalized_text = text_cap.capitalize()
print(capitalized_text) # Output: Hello world

# 12. startswith() - Checks whether the strings starts with the sepcified substring.
text_w = "Hello World"
print(text_w.startswith("Hel")) # Output: True

# 13. endswith() - Checks whether the strings are ending with the specified substring.
text_w = "Hello World"
print(text_w.endswith("rld")) # Output: True

# 14. swapcase() - Swaps upper case and lower case characters.
name = "LuCkEe"
print(name.swapcase()) # Output: lUcKeE

# 15. isalpha() - Used to check whether the characters inside the string are alphabets .
# Returns True if all characters inside the string are alphabets.
# Returns False if any character inside the string is not alphabet.
my_name = "Lakshman"
print(my_name.isalpha()) # Output: True
statement_1 = "Famo1s"
print(statement_1.isdigit()) # Output: False

# 16. isdigit() - Used to check whether the characters inside the string are numbers.
# Returns True if all characters inside the string are numbers.
# Returns False if any character inside the string is not number.
number = "17852"
print(number.isdigit()) # Output: True
number_1 = "824r5"
print(number_1.isdigit()) # Output: False

# 17. isalnum() - Used to check whether the characters in string are alphanumeric(a number or a letter).
# Returns True if all characters inside the string are alphanumeric.
# Returns False if any character inside the string is special character.
sentence_1 = "Python123"
print(sentence_1.isalnum()) # Output: True
sentence_2 = "Python@123"
print(sentence_2.isalnum()) # Output: False

# 18. islower() - Checks whether all characters inside string are in lowercase.
# Returns True if all characters inside the string are in lowercase.
# Returns False if any character inside the string is not in lower case.
Name = "alice"
print(Name.islower()) # Output: True

# 19. isupper() - Checks whether all characters inside string are in uppercase.
# Returns True if all characters inside the string are in uppercase.
# Returns False if any character inside the string is not in uppercase.
Name_1 = "ALICE"
print(Name_1.isupper()) # Output: True

# f-strings
# f-strings are a way to format strings in Python. They allow us to embed expressions inside string literals, using curly braces {}.
my_name = "Lakshman"
age = 18
f_string = f"My name is {my_name} and my age is {age}"
print(f_string)

# Escape Characters 

# New line Character
# \n character ends the line upto it and start another line. Simply it moves the cursor to next line.
text_w = "Hello World"
text_w_1 = "Hello \nWorld"
print(text_w_1) 

# Tab space Character
# \t character is used to push the characters Horizontally.
sentence_3 = "Name:\tLakshman"
sentence_4 = "Age:\t18"
print(sentence_3)
print(sentence_4)

# Quotes in Strings
# \" is used to print quote inside strings.
print("Lakshman\"s House")