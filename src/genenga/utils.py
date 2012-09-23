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
import os


def error(msg):
    print("ERROR: %s" % msg)
    exit(1)


def save_file(path, data):
    with open(path, 'w') as f:
        f.write((data))


def check_existence_file(path):
    if os.path.isfile(path):
        return path
    else:
        error("No such file %s" % path)
        return False


def check_existence_dir(path):
    if not os.path.isdir(path):
        os.mkdir(path)
    if not path.endswith('/'):
        path += '/'
    return path
