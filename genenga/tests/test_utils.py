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
import os
import unittest
from genenga import utils


class UtilsTests(unittest.TestCase):
    """ tests for units module """

    def setUp(self):
        self.file_path = '/tmp/genenga_test'
        self.dir_path = '/tmp/genenga_test_dir/'
        self.data = 'testtesttest'
        utils.save_file(self.file_path, self.data)

    def tearDown(self):
        if os.path.exists(self.dir_path):
            os.rmdir(self.dir_path)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_check_existence_dir(self):
        """ testing check_existence_dir() """
        self.assertTrue(utils.check_existence_dir(self.dir_path))

    def test_save_file(self):
        """ testing saving file """
        with open(self.file_path) as fobj:
            self.assertEquals(fobj.read(), self.data)

    def test_check_existence_file(self):
        """ testing check_existence_file() """
        self.assertTrue(utils.check_existence_file(self.file_path))
