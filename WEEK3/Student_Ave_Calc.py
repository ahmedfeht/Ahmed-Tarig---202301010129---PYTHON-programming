choice = "y"

# Repeat until user chooses N
while choice == "y":

    # Get three quiz marks
    quiz_1 = float(input("Enter Quiz 1 mark: "))
    quiz_2 = float(input("Enter Quiz 2 mark: "))
    quiz_3 = float(input("Enter Quiz 3 mark: "))

    # Calculate average
    average = (quiz_1 + quiz_2 + quiz_3) / 3

    # Show average
    print("Average Mark =", average)

    # Check pass or fail
    if average >= 50:
        print("PASS")
    else:
        print("FAIL")

    # Ask user to continue
    choice = input("Continue? Select Y/N: ").lower()

print("Program Ended")