# -*- coding: utf-8 -*-
"""genenga.address."""


class Address(object):
    """Dict format of Address."""

    def __init__(self, infile):
        """Initialize Address.

        :param str infile: infile path
        """
        self.address_file = infile

    def address(self):
        """convert list of Addresses data from CSV to Dict.

        :rtype: list
        :return: address dict
        """
        address = []
        with open(self.address_file) as fobj:
            # 0: 1 is enable, other than 1 is disable.
            # 1: last_name destination last(family) name (required)
            # 2: first_name1 destination first name (required)
            # 3: first_name2 destination partner first name (optional)
            # 4: address
            # 5: address2 detail address
            # 6: no1 of postal code in Japan
            # 7: no2 of postal code in Japan
            # 8: no3 of postal code in Japan
            # 9: no4 of postal code in Japan
            # 10: no5 of postal code in Japan
            # 11: no6 of postal code in Japan
            # 12: no7 of postal code in Japan

            lines = [line.split(',')
                     for line in fobj
                     if line.split(',')[0] == '1']
            for record in lines:
                if len(record) == 14:
                    address.append(
                        {"last_name": record[1],
                         "first_name1": record[2],
                         "first_name2": record[3],
                         "address": record[4],
                         "address2": record[5],
                         "no1": record[6],
                         "no2": record[7],
                         "no3": record[8],
                         "no4": record[9],
                         "no5": record[10],
                         "no6": record[11],
                         "no7": record[12],
                         "address3": record[13]})
                else:
                    address.append(
                        {"last_name": record[1],
                         "first_name1": record[2],
                         "first_name2": record[3],
                         "address": record[4],
                         "address2": record[5],
                         "no1": record[6],
                         "no2": record[7],
                         "no3": record[8],
                         "no4": record[9],
                         "no5": record[10],
                         "no6": record[11],
                         "no7": record[12]})
        return address
