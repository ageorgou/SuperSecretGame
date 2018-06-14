Tested with Python 2.7

Adjust instructions based on installation and data directories

- (Setup: `conda create -n game python=2.7`)
- Install Scribus, at least version 1.5 (tested with 1.5.4)
- Run ScribusGeneratorCLI: `./ScribusGeneratorCLI.py ~/SuperSecretGame/bad/bad_card_template.sla -c ~/SuperSecretGame/bad/bad_cards.csv
`
- Create PDFs from the generated .sla files: `/Applications/Scribus.app/Contents/MacOS/Scribus -g -py to-pdf.py ~/SuperSecretGame/bad`
- Repeat for the other directories
