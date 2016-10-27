#-*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE

__location__ = os.path.dirname(os.path.realpath(__file__))

images = "/home/bcadmin/Projects/RNYImages/asp"
outPath = "/home/bcadmin/Projects/ResearchingNY2016/ocrASP"


fileTotal = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileTotal = fileTotal + 1

fileCount = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileCount = fileCount + 1
		path = os.path.join(root, file)
		out = os.path.join(outPath, os.path.splitext(file)[0].split("-")[0])
		if not os.path.isdir(out):
			os.mkdir(out)
		print ("Reading file " + str(fileCount) + " of " + str(fileTotal))
		process = Popen(['tesseract', path, os.path.join(out, os.path.splitext(file)[0])], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
		