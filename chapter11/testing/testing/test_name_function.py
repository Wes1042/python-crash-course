import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """Test for 'name_fucntion.py"""

    def test_first_last_name(self):
        """Do name like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name,'Janis Joplin')
        #setting a result we want to get back.

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Adeaus Mozart work?"""
        formatted_name = get_formatted_name(
            'wolfgang','mozart', 'amadeus')
        self.assertEqual(formatted_name,'Wolfgang Amadeus Mozart')
unittest.main()