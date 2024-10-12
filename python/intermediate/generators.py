# Generators in python


def foo():
    for i in range(5):
        yield i


# for i in list(foo()):
#     print(i)

generator = foo()

print(next(generator))  # 0
print(next(generator))  # 1
print(next(generator))  # 2
print(next(generator))  # 3
print(next(generator))  # 4

# Fibonacci sequence

# 0 1 1 2 3 5 8 13 21...


def fibonacci(size: int):
    a = 0
    b = 1

    for _ in range(size):
        a, b = b, a + b

        yield b


print("============ Fibonacci series ==================")

fibonacci_generator = fibonacci(100)

print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))
print(next(fibonacci_generator))


# Exercise

# * Write a Python program that creates a generator function that generates the next palindrome number after a given number.

# * palindrome_generator(1) 2 3 4 5 6 7 8 9 11 22 33 