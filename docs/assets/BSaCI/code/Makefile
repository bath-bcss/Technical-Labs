paper.pdf: paper.tex plot-data.png
	pdflatex paper.tex

plot-data.png: data.dat plot.py
	python plot.py -i data.dat -o plot-data.png

