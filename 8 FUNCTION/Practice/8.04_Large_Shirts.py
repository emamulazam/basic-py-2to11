''' Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message. '''

def make_shirt(size= "large", message= "I love python."):
    print("The size of the sthir is " + size.title())
    print(message)

make_shirt()
make_shirt(size= "medium")
make_shirt(size= "small", message= "Hi")