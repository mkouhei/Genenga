# -*- coding: utf-8 -*-
"""
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012 Kouhei Maeda <mkouhei@palmtb.net>

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
import sys
import unittest
import argparse
from genenga import command as c


class utilsTests(unittest.TestCase):
    def setUp(self):
        self.prs = argparse.ArgumentParser(description='usage')
        sys.argv = ['', 'example/address.csv']

    def test_parse_options(self):
        """self.assertEqual('', c.parse_options())"""

    def test_set_option(self):
        c.set_option(self.prs, 'destdir')

        self.assertTrue(
            isinstance(
                self.prs.__dict__.get('_option_string_actions').get('-d'),
                argparse._StoreAction)
            )

        c.set_option(self.prs, 'template_path')
        self.assertTrue(
            isinstance(
                self.prs.__dict__.get('_option_string_actions').get('-t'),
                argparse._StoreAction)
            )

    def test_generate_atena(self):
        pass

    def test_main(self):
        pass
