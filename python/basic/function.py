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


guessing_game()
