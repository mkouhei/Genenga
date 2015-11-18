# -*- coding: utf-8 -*-
"""genenga.tests.test_address."""
import unittest
from genenga import address as a


class AddressTests(unittest.TestCase):
    """ tests for address module """

    def setUp(self):
        self.infile = 'example/address.csv'
        self.dict = {}
        self.address = [
            {'no7': '0',
             'name2': 'ねこちゃん',
             'name1': '子猫にゃんこ',
             'no4': '0', 'no5': '0', 'no6': '0',
             'address': '東京都中央区ねこまた町０ー０',
             'no1': '0', 'no2': '0', 'no3': '0'},
            {'no7': '0\n', 'name2': '',
             'name1': '猫山にゃんごろ',
             'no4': '0', 'no5': '0', 'no6': '0',
             'address': '東京都太田区ねこむら町０ー０',
             'no1': '0', 'no2': '0', 'no3': '0'},
            {'no7': '0\n',
             'name2': 'にゃんこ',
             'name1': '猫村にゃん太',
             'no4': '0', 'no5': '0', 'no6': '0',
             'address': '東京都新宿区ねこ町０ー０',
             'no1': '0', 'no2': '0', 'no3': '0'},
            {'no7': '0', 'name2': 'ねこ助',
             'name1': '猫野ねこ太',
             'no4': '0', 'no5': '0', 'no6': '0',
             'address': '神奈川県横浜市こねこ町０ー０',
             'no1': '0', 'no2': '0', 'no3': '0'}]

    def test_addrss(self):
        """ tesging address() """
        addr = a.Address(self.infile)
        self.assertFalse(self.dict, addr.address())
        self.assertTrue(self.address, addr.address())
