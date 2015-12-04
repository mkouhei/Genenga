# -*- coding: utf-8 -*-
"""genenga.control."""
import os
import sys
import pystache
from genenga import address, utils


def generate_atena_tex(template, address_file, outfile_path):
    """generate atena TeX file.

    :param str template: template dictionary
    :param str address_file: address list csv file
    :param str outfile_path: output TeX file path
    """
    renderer = pystache.Renderer(file_encoding='utf-8',
                                 search_dirs=template.get('search_dirs'),
                                 string_encoding='utf-8')
    # set template
    tmpl = renderer.load_template(template.get('template_name'))

    # load address data
    addresses = address.csv2addr(address_file)

    # generate atena TeX data
    if sys.version_info > (2, 6) and sys.version_info < (3, 0):
        data = renderer.render(tmpl, addresses).encode('utf-8')
    elif sys.version_info > (3, 1):
        # pylint: disable=redefined-variable-type
        data = renderer.render(tmpl, addresses)

    with open(outfile_path, 'w') as fobj:
        fobj.write(data)


def generate_atena(convt):
    """generate atena.

    :param `convert.Convert` convt: intermediate object for converting address.
    """
    if convt.address_list and utils.check_existence_file(convt.address_list):
        address_list = convt.address_list
    if utils.check_existence_file(convt.template_path):
        tmpl_path = convt.template_path

    if convt.destdir:
        if utils.check_existence_dir(convt.destdir):
            destdir = os.path.abspath(convt.destdir)
    else:
        destdir = os.path.curdir

    srch_dirs = os.path.dirname(tmpl_path)
    tmpl_name = os.path.basename(tmpl_path).rsplit('.mustache')[0]
    template = {'search_dirs': srch_dirs, 'template_name': tmpl_name}
    outfile_path = os.path.join(destdir, '{0}.tex'.format(tmpl_name))

    generate_atena_tex(template, address_list, outfile_path)
