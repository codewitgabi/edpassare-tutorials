# * value = lambda x: x + 5


def value(x):
    return x + 5


number = 50


def square(number):
    return number**2


print(square(number))
print(square(20))

square_lambda = lambda number: number**2

print(square_lambda(10))

array = [1, 2, 3, 4, 5]


def sum_array(arr):
    # total = 0

    # for i in arr:
    #     total += i

    # return total

    return sum(arr)


sum_array = lambda arr: sum(arr)

print(sum_array([5, 10, 15, 20]))
