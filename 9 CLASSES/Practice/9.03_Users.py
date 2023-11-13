''' Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user's information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user. '''

class User():
    def __init__(self, f_name, l_name, location):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name
        self.location = location

    def describe_user(self):
        print(self.full_name.title() + " live in " + self.location.title() + ".")

    def great_user(self):
            print("Congraculation, " + self.full_name.title())

me = User("emamul", "azam", "barishal")
me.describe_user()
me.great_user()
he = User("helff", "helncc", "hepi")
he.describe_user()
he.great_user()