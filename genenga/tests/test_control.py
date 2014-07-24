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
from genenga import control as c


class ControlTests(unittest.TestCase):
    """ tests for control module """

    def setUp(self):
        self.template = {'search_dirs': 'template/',
                         'template_name': 'address'}
        self.address_file = 'example/address.csv'
        self.outfile_path = '/tmp/address.tex'
        with open('example/address.tex') as fobj:
            self.tex_data = fobj.read()

    def tearDown(self):
        if os.path.exists(self.outfile_path):
            os.remove(self.outfile_path)

    def test_generate_atena_tex(self):
        """ testing generate_atena_tex() """
        c.generate_atena_tex(self.template,
                             self.address_file,
                             self.outfile_path)
        with open(self.outfile_path) as fobj:
            data = fobj.read()
            self.assertEquals(self.tex_data, data)
