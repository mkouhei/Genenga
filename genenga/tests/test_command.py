# -*- coding: utf-8 -*-
"""genenga.tests.test_command."""
import sys
import os
import unittest
import argparse
from genenga import command
# pylint: disable=wrong-import-order
if sys.version_info < (3, 0):
    from StringIO import StringIO
else:
    from io import StringIO


class CommamdTests(unittest.TestCase):
    """tests of command module."""

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
        """testing parse_options()."""
        with self.assertRaises(SystemExit) as error:
            command.parse_options()
        self.assertEqual(2, error.exception.code)
        self.assertTrue(sys.stderr.getvalue())

    def test_set_option_destdir(self):
        """testing set_option()."""
        command.set_option(self.parser, 'destdir')
        self.assertEqual('/tmp',
                         self.parser.parse_args('-d /tmp'.split()).destdir)
        self.assertEqual('/tmp/foo',
                         self.parser.parse_args(
                             '--destdir /tmp/foo'.split()).destdir)

    def test_set_option_address_list(self):
        """testing set_option()."""
        command.set_option(self.parser, 'address_list')
        self.assertEqual('address.csv',
                         self.parser.parse_args(
                             'address.csv'.split()).address_list)

    def test_set_option_template_path(self):
        """testing set_option()."""
        command.set_option(self.parser, 'template_path')
        self.assertEqual('address.mastache',
                         self.parser.parse_args(
                             '-t address.mastache'.split()).template_path)
        self.assertEqual('address.mastache',
                         self.parser.parse_args(
                             '--template_path '
                             'address.mastache'.split()).template_path)

    def test_main_fail(self):
        """test main fail."""
        with self.assertRaises(SystemExit):
            command.main()
