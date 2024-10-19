try:
    # ? Holds the actual perfect code.

    age = int(input("Enter your age: "))

    print("Yeeeee!!!! You passed in the right data", age)
except:
    # ! Handles the user's mistake

    print("Naaaaah!!! You passed in the wrong data")
finally:
    # * Run no matter what, it doesn't care.

    print("Okay, let's go!!")


def divide(first_number, second_number):
    try:
        return first_number / second_number

    except ZeroDivisionError:
        return "Cannot divide by Zero"

    except TypeError:
        return "Dude!! Why are you trying to divide by a word???"

    except Exception as e:
        return e


print(divide(5, 2))
print(divide(4, 2))
print(divide(2, 4))
print(divide(4, 0))
print(divide(2, "Elizabeth"))


def add(first_number, second_number):
    if not isinstance(first_number, int):
        raise ValueError("First number must be an actual number")

    # if not isinstance(second_number, int):
    #     raise Exception("Second number must be an actual number")

    assert isinstance(first_number, int), "First number must be an actual number"
    assert isinstance(second_number, int), "Second number must be an actual number"

    return first_number + second_number


print("\n=========== Add number =========")

print(add(1, 5))
print(add(5, -2))
print(add("Coder", "Elizabeth"))


# * Assignment

"""
* Write a Python program that prompts the user to input a number and handles a KeyboardInterrupt exception if the user cancels the input.

* Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.
"""
