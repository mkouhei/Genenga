# -*- coding: utf-8 -*-
"""genenga.tests.test_control."""
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
