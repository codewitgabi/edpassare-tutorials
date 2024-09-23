# Sets

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 2, 1, 4]

my_set = set(list_)  # {1, 2, 3, 4, 5, 6, 7, 8}

print(dir(my_set))

# Adding to a set

my_set.add(True)

print("My set", my_set)

# Remove from a set

my_set.remove(1)
# my_set.remove(10)
my_set.discard(10)

print("My set", my_set)

copy_set = my_set.copy()

print("Copy set", copy_set)

# Clearing a set

copy_set.clear()

print("Copy set after it was cleared", copy_set)


# Popping a value from a set

my_set.pop()

print("My set", my_set)

# Intersection

setA = {1, 2, 5}
setB = {1, 5, 4}

print("Intersection of setA and setB is", setA.intersection(setB))

# Union

print("Union of setA and setB is", setA.union(setB))  # {1, 2, 5, 4}


"""
Assignments:

Task 1: Given three lists, find the common elements in the three lists 

Input : ar1 = [1, 5, 10, 20, 40, 80]
        ar2 = [6, 7, 20, 80, 100]
        ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Output : [80, 20]

Input : ar1 = [1, 5, 5]
        ar2 = [3, 4, 5, 5, 10]
        ar3 = [5, 5, 10, 20]

Output : [5]

Task 2: Write a python program to convert a set into a tuple and vice versa

Input: {'a', 'b', 'c', 'd', 'e'}
Output: ('a', 'c', 'b', 'e', 'd')

Input: ('x', 'y', 'z')
Output: {'z', 'x', 'y'}
"""
