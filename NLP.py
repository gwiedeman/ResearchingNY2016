from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import os
#java_path = "/usr/lib/jvm/java-7-openjdk-amd64" # replace this
#os.environ['JAVAHOME'] = java_path

wordToke = WordPunctTokenizer()
stanfordPath = "/home/bcadmin/Projects/RNYImages/stanford-ner-2015-12-09"
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.6.0.jar'))

dataPath = "/home/bcadmin/Projects/ResearchingNY2016/ocr"
outPath = "/home/bcadmin/Projects/ResearchingNY2016/output"

fileTotal = 0
for root, dirs, files in os.walk(dataPath):
	for file in files:
		fileTotal = fileTotal + 1

fileCount = 0
for root, dirs, files in os.walk(dataPath):
	for file in files:
		fileCount = fileCount + 1
		text = os.path.join(root, file)
		print ("Reading file " + str(fileCount) + " of " + str(fileTotal))

		#for testing
		#if 1 == 1:

		dataFile = open(text, 'r')
		sourceText = dataFile.read()

		orgs = open(os.path.join(outPath, "organizations.csv"), "a")
		peeps = open(os.path.join(outPath, "people.csv"), "a")
		places = open(os.path.join(outPath, "locations.csv"), "a")
		for tagged in st.tag(wordToke.tokenize(sourceText)):
			print (tagged)
			if tagged[1] == 'ORGANIZATION':
				orgs.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)

			if tagged[1] == 'PERSON':
				peeps.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)

			if tagged[1] == 'LOCATION':
				places.write("\n" + tagged[0] + "|" + os.path.basename(root) + "|" + file)




		

		dataFile.close()
		orgs.close()
		peeps.close()
		places.close()