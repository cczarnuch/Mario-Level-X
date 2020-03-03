LATEX=pdflatex -interaction nonstopmode

ProblemStatement.pdf: ProblemStatement.tex
	$(LATEX) $?

default:
	ProblemStatement.pdf

clean:
	rm *.aux *.log

cleanall:
	rm *.aux *.log *.pdf
