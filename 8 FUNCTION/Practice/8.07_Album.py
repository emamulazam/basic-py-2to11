''' Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album's dictionary. Make at least one new
function call that includes the number of tracks on an album. '''

def make_alfum(artist_name, album_title):
    music = {'name': artist_name, 'title': album_title}
    return music

x = 0
while True:
    x = x + 1
    print("\nPlease tell me your name:")
    name = input("Artist name: ")
    if name == 'q':
        break
    album = input("Album title: ")

    artist_album = make_alfum(name, album)
    print(str(x) + ". " + str(artist_album))

print("You dectionary is end")