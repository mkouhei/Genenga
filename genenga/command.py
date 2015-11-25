# -*- coding: utf-8 -*-
"""genenga.command."""
import argparse
from genenga import utils, control, convert, __version__


def parse_options():
    """parse options."""
    prs = argparse.ArgumentParser(description='usage')
    prs.add_argument('-v', '--version',
                     action='version',
                     version=__version__)
    set_option(prs, 'destdir')
    set_option(prs, 'address_list')
    set_option(prs, 'template_path')
    return prs.parse_args()


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


def main():
    """main function."""
    try:
        convt = convert.Convert()
        convt.convert_from_argparse(parse_options())
        control.generate_atena(convt)
    except RuntimeError as error:
        utils.error(error)
    except UnboundLocalError as error:
        utils.error(error)


if __name__ == '__main__':
    main()
