from unittest import TestCase
from Robione_na_zajeciach.silnia import silnia, NotIntErr


class TestSilnia(TestCase):
    def test_silnia(self):
        self.assertEqual(silnia(0), 1)

    def test_badargument(self):
        with self.assertRaises(NotIntErr):
            silnia("Dwa")

