# Loops Practice
# Loops allow us to execute a block of code repeatedly as long as a specified condition is true.

# 1. For Loop
# A for loop is used to iterate over a sequence (like a list, tuple, string) or other iterable objects.
# Example: Print numbers from 1 to 5 using a for loop.
for i in range(1,6):
    print(i) # The range() function add elements dynamically to the sequence. Start value is inclusive and end value is exclusive.

# 2. Nested For Loop
# A nested for loop is a for loop inside another for loop.
# Example: prints a 3x3 grid of asterisks (*) 
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print() # This empty print() is used to move to next line.

# 3. While Loop
# A while loop is used to execute a block of code as long as a specified condition is true.
# Example: Print numbers from 1 to 5 using a while loop.
i = 1
while i <= 5:
    print(i)
    i = i + 1 # This is used to increment the value of i by 1 in each iteration.

# 4. Nested While Loop
# A nested while loop is a while loop inside another while loop.
# Example: prints a 3x3 grid of asterisks (*)
i = 0
while i < 3:
    j = 0
    while j < 3:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1

# 5. Break Statement
# The break statement is used to exit a loop prematurely when a certain condition is met.
# Example: Print numbers from 1 to 5, but stop if the number is 3.
for i in range(1,6):
    if i == 3:
        break # This will exit the loop when i is equal to 3.
    print(i) 

# 6. Continue Statement
# The continue statement is used to skip the current iteration of a loop and move to the next iteration.
# Example : Print numbers from 1 to 5, but skip the number 3.
for i in range(1,6):
    if i == 3:
        continue # This will skip the current iteration when i is equal to 3 and move to the next iteration.
    print(i)

# Pass Statement
# The pass statement act as placeholder for future code. It does nothing and avoids syntax errors when a statement is required syntactically but no code needs to be executed.
for i in range(1,6):
    pass # This will do nothing and move to the next iteration. It is used when we want to write code later but want to avoid syntax errors for now.

