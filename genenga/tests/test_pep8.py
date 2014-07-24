# -*- coding: utf-8 -*-
"""
    Copyright (C) 2013 Kouhei Maeda <mkouhei@palmtb.net>

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
import pep8

BASE_PATH = os.path.dirname(os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))))


class PEP8Test(unittest.TestCase):
    """ test of unit test pep 8 style guide """

    def test_pep8(self):
        """ test runner """
        pep8.DEFAULT_EXCLUDE = ('.tox,*.egg,migrations/,'
                                'shiori/bookmark/migrations/')
        pep8style = pep8.StyleGuide([['statistics', True],
                                     ['show-sources', True],
                                     ['repeat', True],
                                     ['paths', [BASE_PATH]]],
                                    parse_argv=False,
                                    config_file=True)
        report = pep8style.check_files()
        assert report.total_errors == 0
