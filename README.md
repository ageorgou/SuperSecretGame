Tested with Python 2.7

Adjust instructions based on installation and data directories

- (Setup: `conda create -n game python=2.7`)
- Install Scribus, at least version 1.5 (tested with 1.5.4)
- Run ScribusGeneratorCLI:
```
cd input
/Applications/Scribus.app/Contents/share/scribus/scripts/ScribusGeneratorCLI.py $PWD/card_template.sla -c $PWD/card_content.csv
```
- Create PDFs from the generated .sla files: `/Applications/Scribus.app/Contents/MacOS/Scribus -g -py to-pdf.py $PWD/`
- Repeat for the other directories
- Convert to png just for sanity check:
`montage *pdf cards.png`
