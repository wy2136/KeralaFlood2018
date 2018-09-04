#!/usr/bin/env python
import glob, os.path
from mypdf import pdf2png

pdfs = glob.glob('figs/*.pdf')
pngs = [pdf.replace('figs', 'img').replace('.pdf', '.png')
    for pdf in pdfs]

for pdf,png in zip(pdfs, pngs):
    if not os.path.exists(png):
        pdf2png(pdffile=pdf, dpi=200, pngfile=png)
        print('Convert:', pdf, '->', png)
    else:
        print('\tExists:', png)
