import unittest
from pluralize_2 import pluralize_string


class TestPluralizeString(unittest.TestCase):

    def test_pluralize_one(self):
        result = pluralize_string(1)
        self.assertEqual(result, '1 программист')
        self.assertTrue(result.endswith('программист'))
        self.assertIn('1', result)
        self.assertRegex(result, r'^\d+ программист$')

    def test_pluralize_two(self):
        result = pluralize_string(2)
        self.assertEqual(result, '2 программиста')
        self.assertNotEqual(result, '2 программист')
        self.assertFalse(result.startswith('программист'))
        self.assertRegex(result, r'^\d+ программиста$')

    def test_pluralize_five(self):
        result = pluralize_string(5)
        self.assertEqual(result, '5 программистов')
        self.assertGreater(len(result), 10)
        self.assertLess(len(result), 20)

    def test_pluralize_twenty_one(self):
        result = pluralize_string(21)
        self.assertEqual(result, '21 программист')
        self.assertCountEqual(result, 'программист21 ')

    def test_pluralize_fifty_three(self):
        result = pluralize_string(53)
        self.assertEqual(result, '53 программиста')


if __name__ == '__main__':
    unittest.main()
