from unittest import TestCase
from spotkanie1.zajecia1_zad5 import vat_faktura, NotListError


class TestVat_faktura(TestCase):

    def test_vat_faktura(self):
        with self.assertRaises(NotListError):
            vat_faktura("fff")

