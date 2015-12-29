# -*- coding: utf-8 -*-
"""genenga.tests.test_utils."""
import os
import unittest
from genenga import utils


class UtilsTests(unittest.TestCase):
    """tests for units module."""

    def setUp(self):
        self.file_path = '/tmp/genenga_test'
        self.dir_path = '/tmp/genenga_test_dir/'
        self.data = 'testtesttest'
        with open(self.file_path, 'w') as fobj:
            fobj.write(self.data)

    def tearDown(self):
        if os.path.exists(self.dir_path):
            os.rmdir(self.dir_path)
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_check_existence_dir(self):
        """testing check_existence_dir()."""
        self.assertTrue(utils.check_existence_dir(self.dir_path))

    def test_check_existence_file(self):
        """testing check_existence_file()."""
        self.assertTrue(utils.check_existence_file(self.file_path))
