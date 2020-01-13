import unittest
from unittest1 import get_function

class NameTestCase(unittest.TestCase):
  def test_first_last_name(self) :
    formatted_name = get_function('janis', 'joplin')
    self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()