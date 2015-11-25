# -*- coding: utf-8 -*-
"""genenga.control."""
import os
import sys
import pystache
from genenga import address, utils

TEMPLATE = '/usr/share/genenga/template/address.mustache'


def generate_atena_tex(template, address_file, outfile_path):
    """generate atena TeX file.

    :param template: template dictionary
    :param address_file: address list csv file
    :param outfile_path: output TeX file path
    """
    s_dirs = template.get('search_dirs')

    renderer = pystache.Renderer(file_encoding='utf-8',
                                 search_dirs=s_dirs,
                                 string_encoding='utf-8')
    # set template
    tmpl = renderer.load_template(template.get('template_name'))

    # load address data
    addresses = address.Address(address_file)

    # generate atena TeX data
    if sys.version_info > (2, 6) and sys.version_info < (3, 0):
        data = renderer.render(tmpl, addresses).encode('utf-8')
    elif sys.version_info > (3, 1):
        data = renderer.render(tmpl, addresses)

    with open(outfile_path, 'w') as fobj:
        fobj.write(data)


def generate_atena(convt):
    """generate atena.

    :param convt: command line arguments
    """
    if convt.address_list:
        if utils.check_existence_file(convt.address_list):
            address_list = convt.address_list
        if utils.check_existence_file(convt.template_path):
            tmpl_path = convt.template_path
    else:
        if utils.check_existence_file(TEMPLATE):
            tmpl_path = TEMPLATE

    if convt.destdir:
        if utils.check_existence_dir(convt.destdir):
            destdir = os.path.abspath(convt.destdir)
    else:
        destdir = './'

    srch_dirs = os.path.dirname(tmpl_path)
    tmpl_name = os.path.basename(tmpl_path).rsplit('.mustache')[0]
    template = {'search_dirs': srch_dirs, 'template_name': tmpl_name}
    outfile_path = os.path.join(destdir, tmpl_name + '.tex')

    generate_atena_tex(template, address_list, outfile_path)
