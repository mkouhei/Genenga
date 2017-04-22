# -*- coding: utf-8 -*-
"""genenga.exceptions."""


class Error(Exception):
    """Base error class."""

    pass


class InvalidFormat(Error):
    """Invalid format."""

    pass


class NotFound(Error):
    """not found."""

    pass
