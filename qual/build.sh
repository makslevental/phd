./clean.sh
set -e
pdflatex -shell-escape quals.tex
pdflatex -shell-escape quals.tex
biber quals
pdflatex -shell-escape quals.tex
