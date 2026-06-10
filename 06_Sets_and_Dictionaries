# Sets and Dictionaries

# Sets 
# A Set is a unordered collections of unique elemnts.
S = {1,4,7,2,5}
print(S)
s = set([1,6,3,8]) # set() function is used to create a set.
print(s)
# Empty Set
s_1 = {} # (wrong) This creates a dictionary
s_1 = set() # Right method.

# Set operations
A = {1,2,3,4}
B = {3,4,5,6}

# 1. Union(|)
# combines both sets.
print(A|B)

# 2. Intersection(&)
# gives common elements in both sets.
print(A&B)

# 3. Difference(-)
# When B is subtracted from A , it gives the elements only present in A and not in B.
print(A-B)

# 4. Symmetric Difference(^)
# Gives the elements that are present in only one set. Simply removing intersection elements from union elements.
print(A^B)

# 5. add()
# used to add elements
A.add(10)
print(A)

# 6. update()
# adds multiple elements
A.update({26,78,54})
print(A)

# 7. remove()
# used to remove an element, gives error when element is not present.
A.remove(10)
print(A)

# 8. discard()
# gives no error when element is not present in the set.
A.discard(10)
print(A)

# 9. pop()
# removes a random element
A.pop()
print(A)

# 10. issubset()
# X.issubset(Y) returns true if X is subset of Y, if not it returns false.
X = {1, 2}
Y = {1, 2, 3, 4}
print(X.issubset(Y))

# 11. issuperset()
# X.issuperset(Y) returns true if X is superset of Y, if not it returns false.
print(Y.issuperset(X))

# 12. isdisjoint()
# X.isdisjoint(Y) returns true if no common elements , if not it returns false.
print(X.isdisjoint(Y))

# Membership checking
print(2 in X)
print(5 in X)

# Frozen set
# This is an immutable set, cannot perform add(), update() etc operations.
fs = frozenset([1,4,6,3])
print(fs)

# Set Comprehension
s = {x*x for x in range(5)}
print(s)

# Dictionaries
# Dictionaries store data in key:value pairs.
person = {"name": "Alice", "age": 30, "city": "Delhi"}
print(person)
coords = dict(x=10, y=20)
print(coords)
from_pairs = dict([("a", 1), ("b", 2)])
print(from_pairs)

# Accessing Values
print(person["name"]) # This method gives error when key is not present in the dictionary.
# get(key, default) - when key is not found it gives the default value mentioned.
print(person.get("state", "not found"))

# Membership checking
print("age" in person)
print("state" not in person)

# Modifying Dictionaries
d = {
    "name":"Ram",
    "age":21
}
# 1. Adding new Key
d["salary"] = 50000
print(d)
# 2. Updating existing key
d["age"] = 25
print(d)
# del method is used to removes key and it does not return value. Raises error when key is not found in the dictionary.
d = {"a": 1, "b": 2, "c": 3}

del d["a"]        # removes key "a", returns nothing
print(d)          # {"b": 2, "c": 3}

# Trying to use its "return value" is a SyntaxError
# x = del d["b"]  gives an syntax error since del is not an expression.

# pop() method removes the key and returns the value.
# pop(key, default value) - this helps us to print the default value when key is not found in the dictionary.
d = {"a": 1, "b": 2, "c": 3}

val = d.pop("a")      # removes "a" AND returns its value
print(val)            # 1
print(d)              # {"b": 2, "c": 3}
val_1 = d.pop("z", 0)
print(val_1)     # 0

d_1 = {"a": 1, "b": 2, "c": 3, "d": 4}
for key in d_1:
    print(key)
for val in d_1.values():
    print(val)
for key,val in d_1.items():
    print(f"{key}->{val}")

# Merging dictionaries
# Always rightmost dictionary wins when there are duplicate keys. 
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = d1 | d2    # Here d2 is rightmost dictionary so b value is 99.
print(merged)  
merged_1 = d2 | d1   # Here d1 is rightmost dictionary so b value is 2.
print(merged_1) 

# Dictionary Comprehension
squares = {x: x**2 for x in range(1, 6)}
print(squares) # {1:1, 2:4, 3:9, 4:16, 5:25}

filtered = {k: v for k, v in squares.items() if v > 5}
print(filtered) # {3:9, 4:16, 5:25}
