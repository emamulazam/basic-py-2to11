while True:
    name = input("Enter your name: ")
    if name == "q" or name == "Q":
        break
    else:
        with open('guest_book.txt', 'a') as book:
               book.write(name.title() + "\n")
