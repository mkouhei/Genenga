======================================================
Genenga is generator PDF of Nengajo from address list.
======================================================

Requirement
-----------

Debian Packages
^^^^^^^^^^^^^^^

* mendexk
* texlive-binaries
* nkf
* libc-bin
* python2.x
* fonts-vlgothic
* fonts-aoyagi-kouzan-t
* fonts-umeplus
* make
* ptex-bin
* pystache (but yet current ITP)

address.csv format
------------------

address list is CSV. It is syntax is below::

   flag,PersonName1,PersonName2,address,zipcode1,zipcode2,zipcode3,zipcode4,zipcode5,zipcode6,zipcode7


example
^^^^^^^
::

   1,猫にゃんこ,ねこちゃん,東京都中央区ねこまた町０ー０,0,0,0,0,0,0,0


flag of address first field
^^^^^^^^^^^^^^^^^^^^^^^^^^^

#. target this year.
#. next year target but not sent this year.
#. sent the before last.
#. remove.

Usage
-----

#. Update address.csv
#. convert photo, extractbb photoimage.
#. edit nenga-yoko.tex
#. make, generate nenga-yoko.pdf, print this pdf.
#. ./generate-atena.sh, generate atena.pdf, print this.

