import unittest
from  ans import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        f_name = 'emamul'
        l_name = 'azam'
        annual_salary = 10000
        self.my_employee = Employee(f_name, l_name, annual_salary)

    def test_give_default_raise(self):
        self.info = self.my_employee.give_raise()
        self.assertEqual(self.info, "Emamul Azam 15000")

    def test_give_custom_raise(self):
        self.info = self.my_employee.give_raise(10000)
        self.assertEqual(self.info, "Emamul Azam 20000")

unittest.main()