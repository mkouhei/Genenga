# -*- coding: utf-8 -*-
"""genenga.address."""
import re
from genenga.exceptions import InvalidFormat


class Person(object):
    """Person class."""

    def __init__(self, first_name, last_name=''):
        """initialize Person."""
        if first_name:
            self.first_name = first_name
        else:
            self.first_name = ''
        self.last_name = last_name


class PostalCode(object):
    """The Japanese postal code class."""

    def __init__(self, postal_code):
        """initialize PostalCode."""
        parsed_code = self.parse_postal_code(postal_code)
        self.no0 = parsed_code[0]
        self.no1 = parsed_code[1]
        self.no2 = parsed_code[2]
        self.no3 = parsed_code[3]
        self.no4 = parsed_code[4]
        self.no5 = parsed_code[5]
        self.no6 = parsed_code[6]

    @staticmethod
    def parse_postal_code(postal_code):
        """parse postal code string."""
        pat_numonly = re.compile(r'\A\d{7}(\n)?\Z')
        pat_hyphen = re.compile(r'\A\d{3}-\d{4}(\n)?\Z')
        if pat_numonly.match(postal_code):
            return postal_code.rstrip()
        elif pat_hyphen.match(postal_code):
            return ''.join(postal_code.rstrip().split('-'))
        else:
            raise InvalidFormat('The postal code is not supported format.')


class Address(object):
    """Address class."""

    def __init__(self, *args, **kwargs):
        """initialize Address."""
        self.prefectures = kwargs.get('prefectures')
        self.city = kwargs.get('city')
        self.address = kwargs.get('address')
        self.building = kwargs.get('building')
        self.extra = kwargs.get('extra')

        if args:
            self.address0 = args[0]
            if len(args) > 1:
                self.address1 = args[1]
            if len(args) > 2:
                self.address2 = args[2]
        else:
            self.convert_deprecated()

    def convert_deprecated(self):
        """convert deprecated format."""
        self.address0 = '{0}{1}{2}'.format(self.prefectures,
                                           self.city,
                                           self.address)
        self.address1 = self.building
        self.address2 = self.extra


class Atena(object):
    """Atena."""

    def __init__(self, person, another_person, postal_code, address):
        """Initialize Atena."""
        self.person = person
        self.another_person = another_person
        self.postal_code = postal_code
        self.address = address
