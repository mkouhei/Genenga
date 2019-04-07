# -*- coding: utf-8 -*-
"""genenga.control."""
import os
import sys
import pystache
from pguard import guard
from pguard import guard_cl as g
from genenga import convert
from genenga.exceptions import NotFound


def generate_atena_tex(template, address_file, outfile_path):
    """Generate atena TeX file.

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
    addresses = convert.csv2addr(address_file)

    # generate atena TeX data
    data = guard(
        g(renderer.render(tmpl, addresses), sys.version_info > (3, 1)),
        g(renderer.render(tmpl, addresses).encode('utf-8')))

    with open(outfile_path, 'w') as fobj:
        fobj.write(data)


def check_existence_files(*args):
    """Check exisitence of files.

    :rtype: bool
    :param str path: file path
    """
    for filepath in args:
        if not os.path.isfile(filepath):
            raise NotFound('No such file {0}'.format(filepath))


def check_existence_dir(dirpath=None):
    """Check directory existence.

    :rtype: str
    :return: directory path
    :param str path: directory path
    """
    if dirpath:
        if not os.path.isdir(dirpath):
            os.mkdir(dirpath)
        return dirpath
    return os.path.curdir


def generate_atena(convt):
    """Generate atena.

    :param `convert.Convert` convt: intermediate object for converting address.
    """
    check_existence_files(convt.address_list, convt.template_path)
    destdir = check_existence_dir(convt.destdir)
    srch_dirs = os.path.dirname(convt.template_path)
    tmpl_name = os.path.basename(convt.template_path).rsplit('.mustache')[0]
    template = {'search_dirs': srch_dirs, 'template_name': tmpl_name}
    outfile_path = os.path.join(destdir, '{0}.tex'.format(tmpl_name))
    generate_atena_tex(template, convt.address_list, outfile_path)
