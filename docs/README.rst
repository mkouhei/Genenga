======================================================
Genenga is generator PDF of Nengajo from address list.
======================================================

Requirement
-----------

Debian Packages
^^^^^^^^^^^^^^^

* mendexk
* texlive-binaries
* libc-bin
* python2.7
* fonts-vlgothic
* fonts-aoyagi-kouzan-t
* fonts-umeplus
* make
* ptex-bin
* python-pystache (but yet current ITP)

format of address.csv
---------------------

address list is CSV. It is syntax is below::

   flag,PersonFullName1,PersonFullName2,address,PostalCode1,PostalCode2,PostalCode3,PostalCode4,PostalCode5,PostalCode6,PostalCode7


Example
^^^^^^^
::

   1,子猫にゃんこ,ねこちゃん,東京都中央区ねこまた町０ー０,0,0,0,0,0,0,0
   1,猫山にゃんごろ,,東京都太田区ねこむら町０ー０,0,0,0,0,0,0,0
   1,猫村にゃん太,にゃんこ,東京都新宿区ねこ町０ー０,0,0,0,0,0,0,0
   0,猫太ねこのすけ,,東京都三鷹市こねこ町０ー０,0,0,0,0,0,0,0
   1,猫野ねこ太,ねこ助,神奈川県横浜市こねこ町０ー０,0,0,0,0,0,0,0


Flag of address first field
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. target this year.
#. next year target but not sent this year.
#. sent the before last.
#. remove.

Usage
-----

#. Update address.csv
#. convert photo, extractbb photoimage
#. edit nenga-yoko.tex
#. make, generate nenga-yoko.pdf, print this pdf
#. generate atena.pdf, print this::

   $ genenga address.csv


