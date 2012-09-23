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
import sys
import pystache
from genenga import address
from genenga import utils


def generate_atena_tex(template, address_file, outfile_path):
    """generate atena TeX file

    Arguments:

        template: template dictionary
        address_file: address list csv file
        outfile_path: output TeX file path
    """
    s_dirs = template.get('search_dirs')

    renderer = pystache.Renderer(file_encoding='utf-8',
                                 search_dirs=s_dirs,
                                 string_encoding='utf-8')
    # set template
    renderer.load_template(template.get('template_name'))

    # load address data
    addresses = address.Address(address_file)

    # generate atena TeX data
    if sys.version_info > (2, 6) and sys.version_info < (3, 0):
        data = renderer.render(addresses).encode('utf-8')
    elif sys.version_info > (3, 1):
        data = renderer.render(addresses)

    utils.save_file(outfile_path, data)
