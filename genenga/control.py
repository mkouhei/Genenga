# -*- coding: utf-8 -*-
"""genenga.control."""
import sys
import pystache
from genenga import address


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
