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


