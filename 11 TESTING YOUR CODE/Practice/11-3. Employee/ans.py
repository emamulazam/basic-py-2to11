class Employee():
    def __init__(self, first_name, last_name, annual_salary):
        self.f_name = first_name.title()
        self.l_name = last_name.title()
        self.full_name = self.f_name + " " + self.l_name
        self.annual_salary = annual_salary

    def give_raise(self, add= 5000):
        self.annual_salary += add
        self.info = self.full_name + " " + str(self.annual_salary)
        return self.info
