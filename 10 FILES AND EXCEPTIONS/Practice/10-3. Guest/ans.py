name = input("Enter your name: ")

with open('guest.txt', 'a') as file:
    file.write(name)

print(name.title() + " we store your name in guest.txt")