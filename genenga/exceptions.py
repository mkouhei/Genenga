# -*- coding: utf-8 -*-
"""genenga.exceptions."""


class Error(Exception):
    """Base error class."""

    def __init__(self, message=None):
        """Initialize."""
        super(Error, self).__init__(message)


class InvalidFormat(Error):
    """Invalid format."""

    pass


class NotFound(Error):
    """not found."""

    pass
