''' Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.'''

def favorite_book(book_name):
    print("One of my favortie books is " + book_name.title() 
          + " in Wonderland.")
    
favorite_book("Atomic habit")