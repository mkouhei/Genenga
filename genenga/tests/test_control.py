# -*- coding: utf-8 -*-
"""genenga.tests.test_control."""
import os
import argparse
import unittest
import tempfile
from genenga import command, control
from genenga.exceptions import NotFound


class ControlTests(unittest.TestCase):
    """tests for control module."""

    def setUp(self):
        self.parser = argparse.ArgumentParser(description='usage')
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
        """testing generate_atena_tex()."""
        control.generate_atena_tex(self.template,
                                   self.address_file,
                                   self.outfile_path)
        with open(self.outfile_path) as fobj:
            data = fobj.read()
            self.assertEquals(self.tex_data, data)

    def test_generate_atena(self):
        """testing generate_atena()."""
        command.set_option(self.parser, 'destdir')
        command.set_option(self.parser, 'template_path')
        command.set_option(self.parser, 'address_list')
        args = self.parser.parse_args('-d /tmp/ '
                                      '-t template/address.mustache '
                                      'example/address.csv'.split())
        control.generate_atena(args)
        self.assertTrue(os.path.exists('/tmp/address.tex'))

    def test_check_existence_files(self):
        """check_existence_files test."""
        with self.assertRaises(NotFound):
            control.check_existence_files('/path/to/dummy', '/dummy/file/path')

    def test_check_existence_dir(self):
        """check_existence_dir test."""
        dirpath = tempfile.mkdtemp()
        self.assertEquals(control.check_existence_dir(dirpath), dirpath)
        os.removedirs(dirpath)

    def test_check_existence_dir_nodir(self):
        """check_existence_dir test."""
        dirpath = tempfile.mkdtemp()
        os.removedirs(dirpath)
        self.assertEquals(control.check_existence_dir(dirpath), dirpath)
        os.removedirs(dirpath)

    def test_check_existence_dir_noarg(self):
        """check_existence_dir test."""
        self.assertEquals(control.check_existence_dir(), os.path.curdir)
