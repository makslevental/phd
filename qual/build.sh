./clean.sh
set -e
pdflatex quals.tex
pdflatex quals.tex
biber quals
pdflatex quals.tex
