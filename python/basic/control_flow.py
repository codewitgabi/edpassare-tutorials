"""
This is basically the flow of your project. This is going to explain in detail how your code runs from the top of your python file to the end.

We are going to be talking about conditional statements (if/else/elif/match) and loops (for/while).
"""

# Booleans

# True
# False

orire_is_a_girl = False
orire_is_a_boy = True

# Conditional statements

weather_condition1 = "Rainy"

if weather_condition1 == "Rainy":
    print("It is raining outside, you can put on a sweater")
else:
    print("It is not raining, you can probably put on a sweater")


today = input("What is today? ")

if today == "Monday":
    will_be_going_to_school = True

elif today == "Tuesday":
    will_be_going_to_school = True

elif today == "Wednesday":
    will_be_going_to_school = True

elif today == "Thursday":
    will_be_going_to_school = True

elif today == "Friday":
    will_be_going_to_school = True

elif today == "Saturday":
    will_be_going_to_school = False

elif today == "Sunday":
    will_be_going_to_school = False

else:
    will_be_going_to_school = "We can't say"


print(f"Will I be going to school on {today}", will_be_going_to_school)

#  Loops

print("My name is Michael")

# For loop

for i in range(1000):
    print("My name is Michael")

i = 0
while i < 1000:
    print(i + 1, "My name is Michael")
    i = i + 1

# Assignment

"""
1. There is a popular exercise in programming called fizzbuzz.

Here is your task to complete.

Write a python program that gets a user input, if the number is divisible by 3, print 'Fizz'. If it's divisible by 5, print 'Buzz' and if it's divisible by both 3 and 5, print 'FizzBuzz'.

=> You're most likely going to face challenge with checking if the number is divisible by both 3 and 5. That's why your actual control flow question lie.

2. Calculate the sum of 1 to a given number.:

Say for instance you are given a number 10, add all numbers from 1 up to 10 and print out the sum.

3. Print multiplication table of a given number:

Say you are given the number 5, your program should print this

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30.... up to 5 x 12

Goodluck
"""
