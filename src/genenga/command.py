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

    ----

    Originally, next command in generate-atena.sh.

    ./generate-atena.py | nkf -e > atena.text
    make -f Makfile-atena

    Not need convert to EUC-JP or ISO-2022-JP with nkf now
    why ptex (TeX Live 2012/Debian) supports utf-8.
"""
import argparse
import generator
import utils
from __init__ import __version__


def parse_options():
    prs = argparse.ArgumentParser(description='usage')
    prs.add_argument('-v', '--version', action='version', version=__version__)
    set_option(prs, 'output_file')
    set_option(prs, 'address_list')
    set_option(prs, 'template_path')
    set_option(prs, 'template_name')
    set_option(prs, 'template_encoding')

    args = prs.parse_args()
    return args


def set_option(parser, keyword):
    if keyword == 'output_file':
        parser.add_argument('-o', '--output', action='store',
                            help='specify output TeX file name')
    if keyword == 'address_list':
        parser.add_argument('-a', '--address', action='store', required=True,
                            help='specify input file as address list')
    if keyword == 'template_dir':
        parser.add_argument('-p', '--template_path', action='store',
                            help='specify pystache template path')
    if keyword == 'template_name':
        parser.add_argument('-n', '--template_name', action='store',
                            help='specify pystache template name')
    if keyword == 'template_encoding':
        parser.add_argument('-e', '--template_encoding', action='store',
                            help='specify pystache template encoding')


def main():
    try:
        args = parse_options()
        args.func(args)
    except RuntimeError as e:
        utils.error(e)
    except UnboundLocalError as e:
        utils.error(e)


if __name__ == '__main__':
    main()
