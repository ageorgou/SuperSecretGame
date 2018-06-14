# Produces a PDF for the SLA passed as a parameter.
# Uses the same file name and replaces the .sla extension with .pdf
#
# usage:
# scribus -g -py to-pdf.py file.sla

import glob
import sys

import scribus

directory = sys.argv[-1]
filenames = glob.glob(directory + '/[0-9]*.sla')
if not filenames:
    print("No documents with expected name found in " + directory)
for infile in filenames:
    print("Opening " + infile)
    scribus.openDoc(infile)
    pdf = scribus.PDFfile()
    doc_name = infile.rsplit(".", 1)[0]
    pdf.file = doc_name + ".pdf"
    print("Saving at " + pdf.file)
    pdf.save()
print("Converted %d files" % len(filenames))
