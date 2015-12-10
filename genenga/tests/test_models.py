# -*- coding: utf-8 -*-
"""genenga.tests.test_models."""
import unittest
from genenga import models
from genenga.exceptions import InvalidFormat


class ModelsTests(unittest.TestCase):
    """Test cases for models."""

    def test_person(self):
        """valid person."""
        person = models.Person('Alice', 'Forest')
        self.assertEqual('Alice', person.first_name)
        self.assertEqual('Forest', person.last_name)

        another_person = models.Person('Bob')
        self.assertEqual('Bob', another_person.first_name)
        self.assertEqual('', another_person.last_name)

        some_person = models.Person('', 'Klatt')
        self.assertEqual('', some_person.first_name)
        self.assertEqual('Klatt', some_person.last_name)

    def test_postal_code(self):
        """valid postal code."""
        postal_code = models.PostalCode('1234567')
        self.assertEqual('1', postal_code.no0)
        self.assertEqual('2', postal_code.no1)
        self.assertEqual('3', postal_code.no2)
        self.assertEqual('4', postal_code.no3)
        self.assertEqual('5', postal_code.no4)
        self.assertEqual('6', postal_code.no5)
        self.assertEqual('7', postal_code.no6)

        another_format = models.PostalCode('123-4567')
        self.assertEqual('1', another_format.no0)
        self.assertEqual('2', another_format.no1)
        self.assertEqual('3', another_format.no2)
        self.assertEqual('4', another_format.no3)
        self.assertEqual('5', another_format.no4)
        self.assertEqual('6', another_format.no5)
        self.assertEqual('7', another_format.no6)

    def test_invalid_postal_code(self):
        """invalid postal code."""
        with self.assertRaises(InvalidFormat):
            models.PostalCode('123 4567')

    def test_address_deprecated_format(self):
        """deprecated format address."""
        address = models.Address('東京都中央区ねこまた町〇ー〇')
        self.assertEqual('東京都中央区ねこまた町〇ー〇', address.address0)
        self.assertFalse(hasattr(address, 'address1'))
        self.assertFalse(hasattr(address, 'address2'))

        another_address = models.Address('東京都大田区ねこむら町〇ー〇',
                                         'キャットマンション１０１')
        self.assertEqual('東京都大田区ねこむら町〇ー〇', another_address.address0)
        self.assertEqual('キャットマンション１０１', another_address.address1)
        self.assertFalse(hasattr(another_address, 'address2'))

        some_address = models.Address('東京都新宿区ねこ町〇ー〇',
                                      'またたびストリートマンション',
                                      '四番街１−１０１')
        self.assertEqual('東京都新宿区ねこ町〇ー〇', some_address.address0)
        self.assertEqual('またたびストリートマンション', some_address.address1)
        self.assertEqual('四番街１−１０１', some_address.address2)

    def test_address(self):
        """new format address."""
        address = models.Address(prefectures='東京都',
                                 city='大田区',
                                 address='ねこむら町〇ー〇',
                                 building='キャットマンション１０１')
        self.assertEqual('東京都大田区ねこむら町〇ー〇', address.address0)
        self.assertEqual('キャットマンション１０１', address.address1)
        self.assertIsNone(address.address2)

    def test_atena(self):
        """Atena object."""
        atena = models.Atena(models.Person('Alice', 'Forest'),
                             models.Person('Bob'),
                             models.PostalCode('1234567'),
                             models.Address('東京都中央区ねこまた町〇ー〇'))
        self.assertEqual(atena.person.first_name, 'Alice')
        self.assertEqual(atena.person.last_name, 'Forest')
        self.assertEqual(atena.another_person.first_name, 'Bob')
        self.assertEqual(atena.postal_code.no0, '1')
        self.assertEqual(atena.postal_code.no6, '7')
        self.assertEqual(atena.address.address0, '東京都中央区ねこまた町〇ー〇')
