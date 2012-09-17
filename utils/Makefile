MAKEINDEX:=mendex -f -g
SRCDIR:=.

all: nenga-yoko.pdf
nenga-yoko.dvi: nenga-yoko.tex Makefile

%.pdf: %.dvi
	dvipdfmx -p 148mm,100mm -f template/jis-cjk.map $<


%.dvi: %.tex
	$(MAKE) check
	## end of linting stuff
	platex $< # create draft input
	-$(MAKEINDEX) -s nenga-yoko.ist $(<:%.tex=%)
	platex $< # create draft content with correct spacing for index and toc
	-$(MAKEINDEX) -s nenga-yoko.ist $(<:%.tex=%) # recreate index with correct page number
	platex $< # recreate toc with correct page number

check:
	# check that character code is OK.
	#iconv -f euc-jp -t euc-jp < nenga-yoko.tex > /dev/null
	# specifically check that character code is not iso-2022-jp
	! iconv -f iso-2022-jp -t euc-jp < nenga-yoko.tex > /dev/null
	# check that pre-commit hook is installed.
	# if this fails, please do:

check-precommit:
	make check
	make nenga-yoko.dvi

clean:
	rm -f *~ *.aux *.log *.toc comment.cut
	rm -f *.dvi *.lof *.lot *.idx *.ind *.ilg *.bbl *.blg *.out

cleanall: clean
	rm -f nenga-yoko.pdf

$(PDF):	nenga-yoko.pdf
	cp $< $@

.PHONY: all check clean check-precommit cleanall
