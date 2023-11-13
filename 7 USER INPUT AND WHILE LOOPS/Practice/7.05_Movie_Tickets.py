''' A movie theater charges different ticket prices depending on
a person's age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket. '''


while True:
    try:
        age = int(input("Please enter your age (or type '0' to exit): "))

        if age < 0:
            print("Please enter a valid age.")
        elif age == 0:
            print("Exiting the program. Goodbye!")
            break  # Exit the loop if the user enters '0'
        elif age < 3:
            print("Your movie ticket is free.")
        elif age <= 12:
            print("Your movie ticket costs $10.")
        else:
            print("Your movie ticket costs $15.")
    except ValueError:
        print("Please enter a valid age as a number.")