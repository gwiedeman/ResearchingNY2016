#-*- coding: utf-8 -*-

import os
from subprocess import Popen, PIPE
import time

targetTotal = 18290

print ("sleeping 6 hours")
#sleep 6 hours
time.sleep(21600)
print ("k go")

__location__ = os.path.dirname(os.path.realpath(__file__))

images = "/home/bcadmin/Projects/RNYImages/asp"
outPath = "/home/bcadmin/Projects/ResearchingNY2016/ocrASP"
alertPath = "/media/bcadmin/wwwroot/eresources/UA_requests/alert.txt"

fileTotal = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileTotal = fileTotal + 1
print ("total files found: " + str(fileTotal))

while fileTotal < targetTotal:
	#sleep 30 min
	time.sleep(1800)
	fileTotal = 0
	for root, dirs, files in os.walk(images):
		for file in files:
			fileTotal = fileTotal + 1
	print ("total files found: " + str(fileTotal))
	alertfile = open(alertPath, "w")
	alertfile.write("still waiting... :(\ntotal files found: " + str(fileTotal) + " of " + str(targetTotal))
	alertfile.close()

print ("k go!")
print ("total files found: " + str(fileTotal))

alertfile = open(alertPath, "w")
alertfile.write("k go!\ntotal files found: " + str(fileTotal))
alertfile.close()

fileCount = 0
for root, dirs, files in os.walk(images):
	for file in files:
		fileCount = fileCount + 1
		path = os.path.join(root, file)
		out = os.path.join(outPath, os.path.basename(root))
		if not os.path.isdir(out):
			os.mkdir(out)
		print ("Reading file " + str(fileCount) + " of " + str(fileTotal))
		process = Popen(['tesseract', path, os.path.join(out, os.path.splitext(file)[0])], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()
