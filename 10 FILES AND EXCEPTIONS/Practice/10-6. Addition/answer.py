while True:
    first_number = input("Enter first number: ")
    second_number = input("Enter second number: ")

    if first_number =='q' or second_number == 'q':
        break
    else:
        try:
            ans = int(first_number) + int(second_number)
        except ValueError:
            print("Text could not add.")
        else:
            print(ans)