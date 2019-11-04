import bibtexparser
from fuzzywuzzy import fuzz, process
with open('quals.bib') as bibtex_file:
    bib_database = bibtexparser.load(bibtex_file)


for entry in sorted(bib_database.entries, key=lambda x: x["title"]):
    print(entry["title"])
