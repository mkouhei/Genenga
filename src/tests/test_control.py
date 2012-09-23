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
import unittest
import genenga
from genenga import control as c


class utilsTests(unittest.TestCase):

    def setUp(self):
        self.template = {'search_dirs': 'template/',
                         'template_name': 'address'}
        self.address_file = 'example/address.csv'
        self.outfile_path = '/tmp/address.tex'
        self.tex_data = open('example/address.tex').read()

    def test_generate_atena_tex(self):
        c.generate_atena_tex(self.template,
                             self.address_file,
                             self.outfile_path)
        with open(self.outfile_path) as f:
            data = f.read()
            self.assertEquals(self.tex_data, data)
