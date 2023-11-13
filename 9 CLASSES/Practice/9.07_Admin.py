''' An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator's set of
privileges. Create an instance of Admin, and call your method. '''

class User():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name

    def describe_user(self):
        print(self.full_name.title() + " live in " + self.location.title() + ".")

    def great_user(self):
            print("Congraculation, " + self.full_name.title())

class Admin(User):
     
     def __init__(self, f_name, l_name):
          super().__init__(f_name, l_name)
          self.stores = []

     def show_privileges(self):
          print("Privileges of Admin is:")
          for store in self.stores:
               print("- " + store)

me = Admin("emamul", 'azam')
me.stores = ["can add post", "can delete post", "can ban user"]
me.show_privileges()