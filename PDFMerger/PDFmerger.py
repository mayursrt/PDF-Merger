import PyPDF2
import sys

inputs = sys.argv[1:]

def merge_pdf(pdf_list):
	merger = PyPDF2.PdfFileMerger()
	for pdf in pdf_list:
		print(pdf)
		merger.append(pdf)
	merger.write('merged.pdf')

merge_pdf(inputs)