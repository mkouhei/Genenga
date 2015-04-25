# -*- coding: utf-8 -*-
"""genenga.utils.

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
import sys


def error(msg):
    """print Error mesage and sys.exit(1).

    :param str msg: error message
    """
    print("ERROR: %s" % msg)
    sys.exit(1)


def save_file(path, data):
    """writing data to file.

    :param str path: file path
    :param data: data
    """
    with open(path, 'w') as fobj:
        fobj.write((data))


def check_existence_file(file_path):
    """check exisitence of file.

    :rtype: bool
    :param str path: file path
    """
    if os.path.isfile(file_path):
        return True
    else:
        error("No such file %s" % file_path)
        return False


def check_existence_dir(dir_path):
    """check exisitence of directory.

    :rtype: bool
    :param str dir_path: directory path
    """
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    return dir_path
