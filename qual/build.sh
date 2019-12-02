./clean.sh
set -e
pdflatex --enable-write18 --extra-mem-bot=10000000 --extra-mem-bot=100000000 quals.tex
pdflatex --enable-write18 --extra-mem-bot=10000000 --extra-mem-bot=100000000 quals.tex
biber quals
pdflatex --enable-write18 --extra-mem-bot=10000000 --extra-mem-bot=100000000 quals.tex
