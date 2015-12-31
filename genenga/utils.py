# -*- coding: utf-8 -*-
"""genenga.utils."""
import os
from genenga.exceptions import NotFound


def check_existence_file(file_path):
    """check exisitence of file.

    :rtype: bool
    :param str path: file path
    """
    if os.path.isfile(file_path):
        return True
    else:
        raise NotFound('No such file {0}'.format(file_path))
