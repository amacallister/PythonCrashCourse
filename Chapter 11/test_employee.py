import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee."""

    def setUp(self):
        """Create an employee."""
        self.employee = Employee('dana', 'scully', 100000)

    def test_give_default_raise(self):
        """Test the default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 105000)

    def test_give_custom_raise(self):
        """Test the custom raise works properly."""
        self.employee.give_raise(100000)
        self.assertEqual(self.employee.annual_salary, 200000)


if __name__ == '__main__':
    unittest.main()