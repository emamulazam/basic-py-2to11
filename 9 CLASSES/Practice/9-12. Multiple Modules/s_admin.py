from s_user import User

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