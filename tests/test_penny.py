import unittest
from penny import *

class TestPenny(unittest.TestCase):
    def setUp(self):
        self._p = Penny()

    def test_penny_reads_card_front_and_back(self):
        self._p.read([
            "[front]",
            "Cake",
            "[back]",
            "A yummy dessert",
        ])
        self.assertEqual(self._p.cards(), [Card("Cake", "A yummy dessert")])

    def test_penny_reads_multiple_cards_front_and_back(self):
        self._p.read([
            "[front]",
            "Python",
            "[back]",
            "A coding language",
            "developed in C",
            "[front]",
            "C++",
            "[back]",
            "The best coding language",
        ])
        self.assertEqual(self._p.cards(), [
            Card("Python", "A coding language\ndeveloped in C"),
            Card("C++", "The best coding language"),
        ])

if __name__ == '__main__':
    unittest.main()