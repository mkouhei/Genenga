#!/bin/sh -e

./generate-atena.py | nkf -e > atena.tex
make -f Makefile-atena 
