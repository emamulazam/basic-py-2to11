class User():
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name
        self.full_name = self.f_name + ' ' + self.l_name

    def describe_user(self):
        print(self.full_name.title() + " live in " + self.location.title() + ".")

    def great_user(self):
            print("Congraculation, " + self.full_name.title())




