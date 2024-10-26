try:
    number = int(input("Enter a number: "))
except KeyboardInterrupt:
    print("\nYou interrupted the flow with Ctrl + C")
except ValueError:
    print("You were asked to enter a number not something else")
    