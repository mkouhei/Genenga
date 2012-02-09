# Requirement #

## Debian Packages ##

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

## address.csv format ##

```csv
flag,PersonName1,PersonName2,address,zipcode1,zipcode2,zipcode3,zipcode4,zipcode5,zipcode6,zipcode7
```

### example ###

```csv
1,猫にゃんこ,ねこちゃん,東京都中央区ねこまた町０ー０,0,0,0,0,0,0,0
```

## flag is ##

1. target this year.
2. next year target but not sent this year.
3. sent the before last.
4. remove.

### Usage ###

1. Update address.csv
2. convert photo, extractbb photoimage.
3. edit nenga-yoko.tex
4. make, generate nenga-yoko.pdf, print this pdf.
5. ./generate-atena.sh, generate atena.pdf, print this.
 
