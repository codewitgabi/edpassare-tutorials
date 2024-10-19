db_username = "Orire"
db_password = "12345"

# username = input("Enter your username: ")
# password = input("Enter your password: ")

# if username == db_username and password == db_password:
#     print("Login successful")
# else:
#     print("Invalid username or password")

# username = input("Enter your username: ")
# password = input("Enter your password: ")


"""
def function_name():
    # code here
"""


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == db_username and password == db_password:
        print("Login successful")
    else:
        print("Invalid username or password")

        login()


# login()

correct_guess = 5


def guessing_game():
    user_guess = input("Enter a guess: ")

    if int(user_guess) == correct_guess:
        print("Congratulations!!!!!")
    else:
        print("Sorry, that's not the correct guess.")

        # User has to guess again

        guessing_game()


# guessing_game()

"""
* DRY -> Don't repeat yourself
"""

# * Function parameters and arguments


def add_numbers(first_number, second_number):
    # * Parameters are passed when defining a function
    # * Arguments are passed when calling a function

    return first_number + second_number


solution = add_numbers(12, 34)

print(solution)

# print(add_numbers(9, 50))
# print(add_numbers(2, 2))
# print(add_numbers(5, 0))
# print(add_numbers(5, -4))
# print(add_numbers(6, 10))


# * Types of arguments in a function

# * 1. Positional argument
# * 2. Keyword argument
# * 3. Optional parameters


def positional_argument(a, b, c):
    print("a", a)
    print("b", b)
    print("c", c)


# positional_argument(1, 2, 3)


def keyword_argument(a, b=None, c=None):
    print("a", a)
    print("b", b)
    print("c", c)


keyword_argument(1, c="Ruth", b="Orire")

# * Rule => Positional argument cannot come after a keyword argument

"""
* Assignment

? Write a function to perform the following actions

* Subtract numbers => subtract_numbers() => Use positional arguments only
* Multiply numbers => multiply_numbers() => Use keyword arguments only
* Divide numbers using float division => divide_numbers() => Use positional and keyword arguments
* Get remainder when two numbers are divided => get_remainder() => Use positional arguments only

! Your functions should only use the return keyword and not print directly from it.
"""
