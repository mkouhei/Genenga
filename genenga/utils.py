# -*- coding: utf-8 -*-
"""genenga.utils."""
import os
import sys


def error(msg):
    """print Error mesage and sys.exit(1).

    :param str msg: error message
    """
    print("ERROR: %s" % msg)
    sys.exit(1)


def check_existence_file(file_path):
    """check exisitence of file.

    :rtype: bool
    :param str path: file path
    """
    if os.path.isfile(file_path):
        return True
    else:
        error("No such file %s" % file_path)
        return False


def check_existence_dir(dir_path):
    """check exisitence of directory.

    :rtype: bool
    :param str dir_path: directory path
    """
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)
    return dir_path
