# -*- coding: utf-8 -*-
"""
    Copyright (C) 2012-2014 Kouhei Maeda <mkouhei@palmtb.net>

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
import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
from genenga import __version__


class Tox(TestCommand):
    user_options = [('tox-args=', 'a', 'Arguments to pass to tox')]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        import shlex
        if self.tox_args:
            errno = tox.cmdline(args=shlex.split(self.tox_args))
        else:
            errno = tox.cmdline(self.test_args)
        sys.exit(errno)


classifiers = [
    "Development Status :: 3 - Alpha",
    "License :: OSI Approved :: "
    "GNU General Public License v3 or later (GPLv3+)",
    "Intended Audience :: End Users/Desktop",
    "Natural Language :: Japanese",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Programming Language :: Python :: Implementation :: CPython",
    "Programming Language :: Python :: Implementation :: PyPy",
    "Topic :: Text Processing :: Markup :: LaTeX",
]

long_description = (open("README.rst").read() +
                    open(os.path.join("docs", "HISTORY.rst")).read())

requires = ['setuptools',
            'pystache']

with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

setup(name='genenga',
      version=__version__,
      description=('Generate Nengajo(Japanese new year card) pdf '
                   'from address list.'),
      long_description=long_description,
      author='Kouhei Maeda',
      author_email='mkouhei@palmtb.net',
      url='https://github.com/mkouhei/GenNenga',
      license='GNU General Public License version 3',
      classifiers=classifiers,
      packages=find_packages(),
      data_files=[('share/genenga/example',
                   ['example/address.csv',
                    'example/address.tex',
                    'example/cat.jpg',
                    'example/cat.xbb',
                    'example/nenga-yoko.tex']),
                  ('share/genenga/template',
                   ['template/address.mustache',
                    'template/jis-cjk.map',
                    'template/vlpgothic.map'])],
      install_requires=requires,
      tests_require=['tox'],
      cmdclass={'test': Tox},
      entry_points="""
        [console_scripts]
        genenga = genenga.command:main
""",)
