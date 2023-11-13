''' Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0. '''

class User():
    def __init__(self):
        self.login_attemts = 0

    def login_attemt(self):
        self.login_attemts += 1
        
    
    def reset_login_attempts(self):
        self.login_attemts = 0
        print(self.login_attemts)

    def increment_login_attempts(self):
        print(self.login_attemts)


me = User()

me.login_attemt()
me.login_attemt()
me.login_attemt()
me.login_attemt()
me.login_attemt()
me.login_attemt()
me.login_attemt()
me.login_attemt()
me.increment_login_attempts()
me.reset_login_attempts()
