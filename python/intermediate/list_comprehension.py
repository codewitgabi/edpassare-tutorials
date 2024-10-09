arr = []

# / Flaot division
# // Int deivision
# % Remainder division

for i in range(10):
    if i % 2 == 0:
        arr.append(i)

print("arr =", arr)


# List comprehension

# newlist = [expression for item in iterable if condition == True]

array = [i for i in range(10) if i % 2 == 0]
print("array", array)
