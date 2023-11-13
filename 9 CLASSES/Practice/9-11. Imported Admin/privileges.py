class User():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name

    def describe_user(self):
        print(self.full_name.title() + " live in " + self.location.title() + ".")

    def great_user(self):
            print("Congraculation, " + self.full_name.title())

class Privileges():
    def __init__(self):
        self.privilege = []
        
    def show_privilege(self):
        print("Privileges of Admin is:")
        for store in self.privilege:
            print("- " + store)

class Admin(User):
     
     def __init__(self, f_name, l_name):
          super().__init__(f_name, l_name)
          self.privileges = Privileges()


me = Admin("emamul", 'azam')
me.privileges.privilege = ["can add post", "can delete post", "can ban user"]
me.privileges.show_privilege()
print(me.privileges.privilege)