"""
* Tuples:

- Tuples are used to store multiple items in a single variable.

- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

- A tuple is a collection which is ordered and unchangeable (immutable).
"""

# Creating a tuple

my_tuple = (1, True, "Amelia")

print("my_tuple", my_tuple)

# Accessing elements in a tuple

"""
Tuples just like every other built-in data structure uses indexing to access elements.
"""

print(my_tuple[0])  # 1
print(my_tuple[1])  # True
print(my_tuple[2])  # Amelia

# Slicing a tuple

print(my_tuple[:2])  # (1, True)
print(my_tuple[1:-1])  # (True,)
print(my_tuple[:])  # (1, True, 'Amelia')
print(my_tuple[::-1])  # ('Amelia', True, 1) Reverses the tuple

# Deleting an item in a tuple (Not possible)

try:
    del my_tuple[0]
except Exception:
    print("An error occurred while deleting an item in a tuple")

# Modifying an item in a tuple (Not possible)

try:
    my_tuple[0] = 2
except Exception:
    print("An error occurred while modifying an item in a tuple")

# Methods in a tuple

"""
Just a little take-home trick, it's very easy to get methods without memorizing them. Therefore, DO NOT try to memorize of 'cram' these methods. I will show you how to do that.
"""

print(
    my_tuple.count(True)
)  # 2 Returns the number of occurence of the item in the tuple.
print(my_tuple.index("Amelia"))  # 2 Returns the index of the item in the tuple

"""
TO GET METHODS THAT CAN BE USED WITH ANY OBJECT IN PYTHON, USE THE dir() function.
"""

print(dir(tuple))

# or

print(dir(my_tuple))


"""Assignment"""

# TASK 1. Practice the above code and ensure to try out everything yourself.
# TASK 2. Once TASK 1 is done, Explain the reason why the code below returned 2 instead of 1.

"""tup = (1, True, 'Me')
print(tup.count(True))
"""
