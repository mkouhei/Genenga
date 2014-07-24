MAKEINDEX:=mendex -f -g
SRCDIR:=.

all: nenga-yoko.pdf
nenga-yoko.dvi: nenga-yoko.tex

%.pdf: %.dvi
	dvipdfmx -p 148mm,100mm -f template/jis-cjk.map $<


%.dvi: %.tex
	## end of linting stuff
	platex $< # create draft input
	-$(MAKEINDEX) -s nenga-yoko.ist $(<:%.tex=%)
	platex $< # create draft content with correct spacing for index and toc
	-$(MAKEINDEX) -s nenga-yoko.ist $(<:%.tex=%) # recreate index with correct page number
	platex $< # recreate toc with correct page number

check-precommit:
	make nenga-yoko.dvi

clean:
	rm -f *~ *.aux *.log *.toc comment.cut
	rm -f *.dvi *.lof *.lot *.idx *.ind *.ilg *.bbl *.blg *.out

cleanall: clean
	rm -f nenga-yoko.pdf

$(PDF):	nenga-yoko.pdf
	cp $< $@

.PHONY: all clean check-precommit cleanall
