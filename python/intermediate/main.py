# Data types

# String

username = "John"
age = "9"

print(type(username))  # str
print(type(age))  # str

# Integer

no_of_students_in_a_class = 10.5  # float
new_age = 9  # int

print(type(no_of_students_in_a_class))
print(type(new_age))

# Boolean

# Can only take two values - True or False

is_it_raining = False
is_today_wednesday = True
did_it_rain_yesternight = True


print(type(is_it_raining))  # bool

# List

students = ["Michael", "Amelia", "Avary", "Jacob"]
# otherStudents = "[John, James, Smith]" # not a list
sentence = [
    "[My name is John and his name is James. This is a list of items I bought at the store => [banana, apples, oranges]",
]

print(type(students))  # list
print(sentence[0])

students[0] = "Gabriel"

print("Students", students)


# Tuple

students_tuple = ("Michael", "Amelia", "Avary", "Jacob")
range_tuple = 1, "Michael", "Amelia", 5
age_tuple = 5, # this is a tuple because it has a comma

print("Range tuple", type(range_tuple))

# students_tuple[0] = "Gabriel"
# print("Student tuple", students_tuple)

# Sets

list_ = [1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 2, 1, 4]

# A set only contains unique values (No duplicate items)

set_ = {1, 2, 3, 4, 5, 6, 7, 8, 2, 4, 2, 1, 4, 0, -1}

print("Set", set_)
