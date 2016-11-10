import os
from subprocess import Popen, PIPE

__location__ = os.path.dirname(os.path.realpath(__file__))

count = 0
for pdfFile in os.listdir(os.path.join(__location__, "pdf")):
	pdfPath = os.path.join(__location__, "pdf", pdfFile)
	outPath = os.path.join(__location__, "ocr", pdfFile.split("-")[1].split(".")[0] + ".txt")
	count = count + 1
	
	process = Popen(['C:\Program Files\mupdf\mutool.exe', 'draw', '-F', 'txt', '-o', outPath, pdfPath], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
	print (stdout)
	print (stderr)