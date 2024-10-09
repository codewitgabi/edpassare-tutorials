range(1, 15, 2)  # 1, 3, 5, 7, 9, 11, 13

print(
    list(range(10))
)  # stop => start as 0 and stop as 10 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
range(5, 100)  # start, stop => start as 5 and stop as 100 [5, 6, 7, ......]
print(
    list(range(5, 100, 5))
)  # start, stop and step => start as 5, stop as 100 and step as 5 [5, 10, 15, 20, .....]


evenArr = []

# float division => / 5 / 2 = 2.5
# int division => // 5 // 3 = 1
# remainder division (modulus) => %

for num in range(1, 10_000):  # [1, 2, 3, 4,...]
    # check if `i` is an even number

    print(num)

    if num % 2 == 0:
        evenArr.append(num)

print(evenArr)

# Using list comprehension

"""
: Syntax

output = [value for...loop condition]
"""

evenArr = [num for num in range(1, 20) if num % 2 == 0]

print(evenArr)

oddArr = [i for i in range(1, 20) if i % 2 != 0]

print(oddArr)
