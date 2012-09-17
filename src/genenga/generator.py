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
    ----

    Modify and fix this script adopt pystache 0.5.2.
"""
import pystache


class Address(pystache.Renderer):

    def __init__(self, file_encoding='utf-8'):
        self.template_path = '.'
        self.template_name = 'address'
        self.template_encoding = 'utf-8'
        self.address_list = 'address.csv'

    def datas(self):
        datas = []
        with open(self.address_list) as f:
            # 0:flag, 1:name1, 2:name2, 3:address,
            # 4:no1, 5:no2, 6:no3, 7:no4, 8:no5, 9:no6, 10:no7
            lines = [line.split(',')
                     for line in f
                     if line.split(',')[0] == '1']
            for l in lines:
                datas.append({
                        "name1": l[1].decode('utf-8'),
                        "name2": l[2].decode('utf-8'),
                        "address": l[3].decode('utf-8'),
                        "no1": l[4],
                        "no2": l[5],
                        "no3": l[6],
                        "no4": l[7],
                        "no5": l[8],
                        "no6": l[9],
                        "no7": l[10]
                        })
        return datas
