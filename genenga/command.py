# -*- coding: utf-8 -*-
"""genenga.command.

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
import argparse
import os.path
from genenga import utils, control, __version__, __template__


def parse_options():
    """parse options."""
    prs = argparse.ArgumentParser(description='usage')
    prs.add_argument('-v', '--version',
                     action='version',
                     version=__version__)
    set_option(prs, 'destdir')
    set_option(prs, 'address_list')
    set_option(prs, 'template_path')

    prs.set_defaults(func=generate_atena)

    args = prs.parse_args()
    return args


def set_option(parser, keyword):
    """set options by keyword.

    :param parser: object of argparser
    :param keyword: keyword of option
    """
    if keyword == 'destdir':
        # output file of directory path
        parser.add_argument(
            '-d', '--destdir', action='store',
            help='destination directory path of output')

    if keyword == 'address_list':
        # address list file path
        parser.add_argument(
            'address_list', action='store',
            help='input file as address list for "atena"')

    if keyword == 'template_path':
        # using template name
        parser.add_argument(
            '-t', '--template_path', action='store', required=True,
            help='pystache template file path')


def generate_atena(args):
    """generate atena.

    :param args: command line arguments
    """
    if args.__dict__.get('address_list'):
        if utils.check_existence_file(args.address_list):
            address_list = args.address_list

    if args.__dict__.get('template_path'):
        if utils.check_existence_file(args.template_path):
            tmpl_path = args.template_path
    else:
        if utils.check_existence_file(__template__):
            tmpl_path = __template__

    if args.__dict__.get('destdir'):
        if utils.check_existence_dir(args.destdir):
            destdir = os.path.abspath(args.destdir)
    else:
        destdir = './'

    srch_dirs = os.path.dirname(tmpl_path)
    tmpl_name = os.path.basename(tmpl_path).rsplit('.mustache')[0]
    template = {'search_dirs': srch_dirs, 'template_name': tmpl_name}
    outfile_path = os.path.join(destdir, tmpl_name + '.tex')

    control.generate_atena_tex(template, address_list, outfile_path)


def main():
    """main function."""
    try:
        args = parse_options()
        args.func(args)
    except RuntimeError as error:
        utils.error(error)
    except UnboundLocalError as error:
        utils.error(error)


if __name__ == '__main__':
    main()
