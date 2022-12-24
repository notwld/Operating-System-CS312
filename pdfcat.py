import os
from PyPDF2 import PdfMerger

x = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfMerger()

for pdf in x:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
