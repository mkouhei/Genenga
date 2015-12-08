# -*- coding: utf-8 -*-
"""genenga.convert."""
from genenga.models import Atena, Person, PostalCode, Address


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


def gen_atena(record):
    """generate atena object."""
    # 1: last name (required)
    # 2: first_name (required)
    # 3: another person's first_name (optional)
    # 4: address (prefectures + city + address)
    # 5: building (optional)
    # 6: extra (optional)
    # 7: no1 of postal code in Japan
    # 8: no2 of postal code in Japan
    # 9: no3 of postal code in Japan
    # 10: no4 of postal code in Japan
    # 11: no5 of postal code in Japan
    # 12: no6 of postal code in Japan
    # 13: no7 of postal code in Japan
    return Atena(Person(record[2], record[1]),
                 Person(record[3], record[1]),
                 PostalCode(''.join([record[i] for i in range(7, 14)])),
                 Address(record[4], record[5], record[6]))


def csv2addr(address_file):
    """convert csv to address."""
    with open(address_file) as fobj:
        lines = [line.split(',') for line in fobj
                 if line.split(',')[0] == '1']
    return dict(address=[atena2dict(gen_atena(record)) for record in lines
                         if record[0] == '1'])


def atena2dict(atena):
    """deprecated."""
    return dict(last_name=atena.person.last_name,
                first_name1=atena.person.first_name,
                first_name2=atena.another_person.first_name,
                address=atena.address.address0,
                address2=atena.address.address1,
                address3=atena.address.address2,
                no1=atena.postal_code.no0,
                no2=atena.postal_code.no1,
                no3=atena.postal_code.no2,
                no4=atena.postal_code.no3,
                no5=atena.postal_code.no4,
                no6=atena.postal_code.no5,
                no7=atena.postal_code.no6)
