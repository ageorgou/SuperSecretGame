# Produces a PDF for the SLA passed as a parameter.
# Uses the same file name and replaces the .sla extension with .pdf
#
# usage:
# scribus -g -py to-pdf.py file.sla

import glob
import sys

import scribus

IMG_TYPE = 2

directory = sys.argv[-1]
filenames = glob.glob(directory + '/[0-9]*.sla')
# Cards whose text is too long, and must therefore use a smaller font
indices_with_long_text = [10, 12, 23, 39, 44, 46, 57]
# HACK! I'm sorry :(
files_with_long_text = ["{}{}.sla".format(directory, i) for i in indices_with_long_text]
if not filenames:
    print("No documents with expected name found in " + directory)
for infile in filenames:
    print("Opening " + infile)
    scribus.openDoc(infile)
    # Auto-scale the picture
    try:
        # Find which image object we must change
        images = [s for s in scribus.getPageItems() if s[1] == IMG_TYPE]
        frame = sorted(images, key=lambda s: s[2])[-1][0]
        # frame should be "Image9" if all elements are rendered
        scribus.setScaleImageToFrame(True, name=frame)
        scribus.saveDoc()
    except NoValidObjectError, err:
        print("Image not found in " + infile)
    # Change the text size if necessary
    print(infile)
    if infile in files_with_long_text:
        print("Found " + infile + "!!!")
        try:
            frame = "Text7"
            scribus.setFontSize(11, frame)
            scribus.saveDoc()
        except NoValidObjectError, err:
            print("Text not found in " + infile)
    # Generate the PDF
    pdf = scribus.PDFfile()
    doc_name = infile.rsplit(".", 1)[0]
    pdf.file = doc_name + ".pdf"
    print("Saving at " + pdf.file)
    pdf.save()
print("Converted %d files" % len(filenames))
