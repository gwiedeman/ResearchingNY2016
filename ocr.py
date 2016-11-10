#-*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE

__location__ = os.path.dirname(os.path.realpath(__file__))

images = "C:\\Users\\Greg\\Pictures\\textbookPhotos"


fileTotal = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileTotal = fileTotal + 1

fileCount = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileCount = fileCount + 1
		path = os.path.join(root, file)
		outpath = os.path.join(__location__, "ocr", os.path.basename(root))
		if not os.path.isdir(outpath):
			os.mkdir(outpath)
		print ("Reading file " + str(fileCount) + " of " + str(fileTotal))
		process = Popen(['tesseract', path, os.path.join(outpath, file)], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()