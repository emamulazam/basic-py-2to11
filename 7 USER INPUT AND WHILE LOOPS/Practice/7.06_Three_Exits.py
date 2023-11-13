''' Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value. '''

active = True  # Set an active variable to control the loop

while active:
    age_input = input("Please enter your age (or type 'quit' to exit): ")

    if age_input.lower() == 'quit':
        print("Exiting the program. Goodbye!")
        active = False  # Set active to False to exit the loop
    else:
        try:
            age = int(age_input)

            if age < 0:
                print("Please enter a valid age.")
            elif age < 3:
                print("Your movie ticket is free.")
            elif age <= 12:
                print("Your movie ticket costs $10.")
            else:
                print("Your movie ticket costs $15.")
        except ValueError:
            print("Please enter a valid age as a number.")
