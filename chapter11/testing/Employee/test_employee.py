import unittest

from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for the module employee"""

    def setUp(self):
        """Make an employee to set up test """
        self.wes = Employee('Wesley' ,'T', 65000)

    def test_give_default_raises(self):
        """Test that the default works """
        self.wes.give_raise()
        self.assertEqual(self.wes.salary,70000)

    def test_give_custom_raise(self):
        """Test that the custom works"""
        self.wes.give_raise(50000)
        self.assertEqual(self.wes.salary,115000)

unittest.main()