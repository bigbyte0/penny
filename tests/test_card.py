import unittest
from card import *

class TestCard(unittest.TestCase):
    def test_cards_are_equal_if_they_have_the_same_front_and_back(self):
        self.assertEqual(Card("Cake", "A tasty dessert"), Card("Cake", "A tasty dessert"))

if __name__ == '__main__':
    unittest.main()
