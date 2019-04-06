# -*- coding: utf-8 -*-
"""genenga.exceptions."""


class Error(Exception):
    """Base error class."""


class InvalidFormat(Error):
    """Invalid format."""


class NotFound(Error):
    """not found."""
