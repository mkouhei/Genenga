#!/usr/bin/env python
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

import pystache

texfile_name = 'atena.tex'
address_list = 'address.csv'

class Address(pystache.View):

    template_path = '.'
    template_name = 'address'
    template_encoding = 'utf-8'

    def datas(self):
        i=0
        datas = []
        for line in open(address_list, 'r'):
            # 0:flag, 1:name1, 2:name2, 3:address,
            # 4:no1, 5:no2, 6:no3, 7:no4, 8:no5, 9:no6, 10:no7
            list = line[:-1].split(',')
            if list[0] == "1":
                
                datas.append({
                    "name1":unicode(list[1], 'utf-8'),
                    "name2":unicode(list[2], 'utf-8'),
                    "address":unicode(list[3], 'utf-8'),
                    "no1":unicode(list[4], 'utf-8'),
                    "no2":unicode(list[5], 'utf-8'),
                    "no3":unicode(list[6], 'utf-8'),
                    "no4":unicode(list[7], 'utf-8'),
                    "no5":unicode(list[8], 'utf-8'),
                    "no6":unicode(list[9], 'utf-8'),
                    "no7":unicode(list[10], 'utf-8')
                    })
        return datas


str = Address().render()
print(str.encode('utf-8'))

