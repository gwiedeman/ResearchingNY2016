import os
from subprocess import Popen, PIPE

pdfDir = "/media/bcadmin/wwwroot/asp_issues"
outDir = "/home/bcadmin/Projects/RNYImages/asp"

fileTotal = 0
for file in os.listdir(pdfDir):
	fileTotal = fileTotal + 1

fileCount = 0
for file in os.listdir(pdfDir):
	fileCount = fileCount + 1

	print ("Converting file " + str(fileCount) + " of " + str(fileTotal))

	pdf = os.path.join(pdfDir, file)
	out = os.path.join(outDir, os.path.splitext(file)[0] + ".png")

	process = Popen(['convert', "-density", "300", "-trim", pdf, "-quality", "100", out], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()