def foo():  # regular function expression
    print(2)

    return "Amelia"


# foo_value = foo()

# print(foo_value)


def bar():  # generator
    yield 1
    yield 2
    yield 10
    yield 4
    yield 5


a = bar()  # a = [1, 2, 10, 4, 5]

# print(next(a))
# print(next(a))
# print(next(a))

def multiples_of_9():
    for i in range(9, 109, 9): # 9 18 .... 99
        yield i

b = multiples_of_9()

print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))

from typing import Generator

def palindromic_number(number: int):
    i = number + 1

    while True:
        if str(i) == str(i)[::-1]:
            return i
        
        i += 1


print(palindromic_number(101))
