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
import os
import sys
import unittest
from genenga import utils as u


class utilsTests(unittest.TestCase):
    def setUp(self):
        self.path = '/tmp/genenga_test'
        self.dirpath = '/tmp/genenga_test_dir/'
        self.data = 'testtesttest'
        u.save_file(self.path, self.data)

    def test_check_existence_dir(self):
        self.assertEquals(self.dirpath,
                          u.check_existence_dir(self.dirpath))

    def test_save_file(self):
        with open(self.path) as f:
            self.assertEquals(f.read(), self.data)

    def test_check_existence_file(self):
        self.assertEquals(self.path,
                          u.check_existence_file(self.path))
