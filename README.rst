========================================================
 Genenga is generator PDF of Nengajo from address list.
========================================================

This utility is generate PDF for printing address "Happy new year card",
a.k.a. "Nengajo" in Japanese.

.. image:: https://secure.travis-ci.org/mkouhei/Genenga.png?branch=master
   :target: http://travis-ci.org/mkouhei/Genenga
.. image:: https://coveralls.io/repos/mkouhei/Genenga/badge.png?branch=master
   :target: https://coveralls.io/r/mkouhei/Genenga?branch=master
.. image:: https://pypip.in/v/Genenga/badge.png
   :target: https://crate.io/packages/Genenga
.. image:: http://readthedocs.org/projects/genenga/badge/?version=latest
   :target: http://genenga.readthedocs.org/en/latest/?badge=latest
   :alt: Documentation Status

Requirement
-----------

Debian Packages
^^^^^^^^^^^^^^^

* texlive-binaries (>= 2017.20170613.44)
* texlive-lang-japanese
* libc-bin
* python2.7 over or python3.5 over
* fonts-takao-gothic
* fonts-takao-mincho
* make
* python-pystache or python3-pystache

format of address.csv
---------------------

address list is CSV. It is syntax is below::

   status,PersonLastName,PersonFirstName1,PersonFirstName2,address,address2,address3,PostalCode1,PostalCode2,PostalCode3,PostalCode4,PostalCode5,PostalCode6,PostalCode7


Example
^^^^^^^
::

   1,子猫,にゃんこ,ねこちゃん,東京都中央区ねこまた町０ー０,,,0,0,0,0,0,0,0
   1,猫山,にゃんごろ,,東京都太田区ねこむら町０ー０,キャットマンション１０１,,0,0,0,0,0,0,0
   1,猫村,にゃん太,にゃんこ,東京都新宿区ねこ町０ー０,,,0,0,0,0,0,0,0
   0,猫太,ねこのすけ,,東京都三鷹市こねこ町０ー０,,,0,0,0,0,0,0,0
   1,猫野,ねこ太,ねこ助,神奈川県横浜市こねこ町０ー０,,,0,0,0,0,0,0,0


.. warning::
   The csv format has changed in v0.5.0. ``address3`` is inserted before ``PostalCode1``.

Flag of address first field
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. target this year.
#. next year target but not sent this year.
#. sent the before last.
#. remove.

Usage
-----

#. Update address.csv

   #. Reset last year status.
   #. Update latest status.
   
#. convert photo, extractbb photoimage
#. edit nenga-yoko.tex
#. make, generate nenga-yoko.pdf, print this pdf
#. generate atena.pdf, print this::

   $ genenga -t path/to/yourtemplate.mustache address.csv


