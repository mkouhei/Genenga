# -*- coding: utf-8 -*-
"""
    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) 2012 Kouhei Maeda <mkouhei@palmtb.net>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


class Address(object):

    def __init__(self, infile):
        self.address_file = infile

    def address(self):
        address = []
        with open(self.address_file) as f:
            # 0: 1 is enable, 0 is not disable
            # 1: name1 destination full name (required)
            # 2: name2 destination partner first name (optional)
            # 3: address
            # 4: no1 of postal code in Japan
            # 5: no2 of postal code in Japan
            # 6: no3 of postal code in Japan
            # 7: no4 of postal code in Japan
            # 8: no5 of postal code in Japan
            # 9: no6 of postal code in Japan
            # 10:no7 of postal code in Japan

            lines = [line.split(',')
                     for line in f
                     if line.split(',')[0] == '1']
            for l in lines:
                address.append({
                        "name1": l[1],
                        "name2": l[2],
                        "address": l[3],
                        "no1": l[4],
                        "no2": l[5],
                        "no3": l[6],
                        "no4": l[7],
                        "no5": l[8],
                        "no6": l[9],
                        "no7": l[10]
                        })
        return address
