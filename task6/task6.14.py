import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
