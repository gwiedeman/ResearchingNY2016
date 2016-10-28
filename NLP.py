from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import os
import time

startTime = time.time()
startTimeReadable = str(time.strftime("%Y-%m-%d %H:%M:%S"))
print ("Start Time: " + startTimeReadable)

wordToke = WordPunctTokenizer()
stanfordPath = "/home/bcadmin/Projects/RNYImages/stanford-ner-2015-12-09"
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.6.0.jar'))

dataPath = "/home/bcadmin/Projects/ResearchingNY2016/ocrASP"
outPath = "/home/bcadmin/Projects/ResearchingNY2016/outASP"
alertPath = "/media/bcadmin/wwwroot/eresources/UA_requests/alert.txt"

fileTotal = 0
for root, dirs, files in os.walk(dataPath):
	for file in files:
		fileTotal = fileTotal + 1

fileCount = 0
for root, dirs, files in os.walk(dataPath):
	for file in files:
		fileCount = fileCount + 1
		looptime = time.time()

		text = os.path.join(root, file)
		print ("Reading file " + str(fileCount) + " of " + str(fileTotal))

		#for testing
		#if 1 == 1:

		dataFile = open(text, 'r')
		sourceText = dataFile.read()

		yearOut = os.path.join(outPath, os.path.basename(root))
		if not os.path.isdir(yearOut):
			os.mkdir(yearOut)

		#totals
		orgs = open(os.path.join(outPath, "total", "organizations.csv"), "a")
		peeps = open(os.path.join(outPath, "total", "people.csv"), "a")
		places = open(os.path.join(outPath, "total", "locations.csv"), "a")
		#years
		orgsY = open(os.path.join(yearOut, "organizations.csv"), "a")
		peepsY = open(os.path.join(yearOut, "people.csv"), "a")
		placesY = open(os.path.join(yearOut, "locations.csv"), "a")


		for tagged in st.tag(wordToke.tokenize(sourceText)):
			#print (tagged)
			if tagged[1] == 'ORGANIZATION':
				orgs.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)
				orgsY.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)

			if tagged[1] == 'PERSON':
				peeps.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)
				peepsY.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)

			if tagged[1] == 'LOCATION':
				places.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)
				placesY.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)

		dataFile.close()
		orgs.close()
		orgsY.close()
		peeps.close()
		peepsY.close()
		places.close()
		placesY.close()

		processTime = time.time() - looptime
		totalTime = time.time() - startTime

		alert1 = "Process took " + str(processTime) + " seconds or " + str(processTime/60) + " minutes or " + str(processTime/3600) + " hours"
		avgTime = totalTime/fileCount
		alert2 = "Average time is " + str(avgTime)
		remaning = fileTotal - fileCount
		alert3 = str(remaning) + " Remaining"
		estimateTime = avgTime*remaning
		alert4 = "Estimated time left: " + str(estimateTime) + " seconds or " + str(estimateTime/60) + " minutes or " + str(estimateTime/3600) + " hours"
		print(alert1)
		print(alert2)
		print(alert3)
		print(alert4)
		
		alertfile = open(alertPath, "w")
		alertfile.write(alert1 + "\n" + alert2 + "\n" + alert3 + "\n" + alert4)
		alertfile.close()
