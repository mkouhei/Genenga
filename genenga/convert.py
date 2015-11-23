# -*- coding: utf-8 -*-
"""genenga.convert."""


class Convert(object):
    """The intermediate object for converting to Address object."""

    def set_param(self, name, value):
        """set name:value property to convert object."""
        setattr(self, name, value)

    def convert_from_argparse(self, args):
        """Convert to artparse.Namespace to Convert object."""
        if hasattr(args, '_get_kwargs'):
            for name, value in vars(args).items():
                self.set_param(name, value)
