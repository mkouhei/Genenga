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
import sys
import os
import unittest
import argparse
from genenga import command as c
if sys.version_info < (3, 0):
    from StringIO import StringIO
else:
    from io import StringIO


class CommamdTests(unittest.TestCase):
    """ tests of command module """

    def setUp(self):
        self.parser = argparse.ArgumentParser(description='usage')
        self.capture = sys.stdout
        self.capture_err = sys.stderr
        sys.stdout = StringIO()
        sys.stderr = StringIO()

    def tearDown(self):
        sys.stdout = self.capture
        sys.stderr = self.capture_err
        if os.path.exists('/tmp/address.tex'):
            os.remove('/tmp/address.tex')

    def test_parse_options_fail(self):
        """ testing parse_options() """
        with self.assertRaises(SystemExit) as error:
            c.parse_options()
        self.assertEqual(2, error.exception.code)
        self.assertTrue(sys.stderr.getvalue())

    def test_set_option_destdir(self):
        """ testing set_option() """
        c.set_option(self.parser, 'destdir')
        self.assertEqual('/tmp',
                         self.parser.parse_args('-d /tmp'.split()).destdir)
        self.assertEqual('/tmp/foo',
                         self.parser.parse_args(
                             '--destdir /tmp/foo'.split()).destdir)

    def test_set_option_address_list(self):
        """ testing set_option() """
        c.set_option(self.parser, 'address_list')
        self.assertEqual('address.csv',
                         self.parser.parse_args(
                             'address.csv'.split()).address_list)

    def test_set_option_template_path(self):
        """ testing set_option() """
        c.set_option(self.parser, 'template_path')
        self.assertEqual('address.mastache',
                         self.parser.parse_args(
                             '-t address.mastache'.split()).template_path)
        self.assertEqual('address.mastache',
                         self.parser.parse_args(
                             '--template_path '
                             'address.mastache'.split()).template_path)

    def test_generate_atena(self):
        """ testing generate_atena() """
        c.set_option(self.parser, 'destdir')
        c.set_option(self.parser, 'template_path')
        c.set_option(self.parser, 'address_list')
        args = self.parser.parse_args('-d /tmp/ '
                                      '-t template/address.mustache '
                                      'example/address.csv'.split())
        c.generate_atena(args)
        self.assertTrue(os.path.exists('/tmp/address.tex'))
