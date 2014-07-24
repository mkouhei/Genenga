# -*- coding: utf-8 -*-
"""
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012-2014 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
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
