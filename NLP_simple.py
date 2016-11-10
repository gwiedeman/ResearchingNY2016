from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import os

__location__ = os.path.dirname(os.path.realpath(__file__))

wordToke = WordPunctTokenizer()
stanfordPath = "/home/bcadmin/Projects/RNYImages/stanford-ner-2015-12-09"
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.6.0.jar'))

dataPath = os.path.join(__location__, "ocrASP")
outPath = os.path.join(__location__, "outASP")

for root, dirs, files in os.walk(dataPath):
	for file in files:

		text = os.path.join(root, file)

		dataFile = open(text, 'r')
		sourceText = dataFile.read()

		orgs = open(os.path.join(outPath, "total", "organizations.csv"), "a")
		peeps = open(os.path.join(outPath, "total", "people.csv"), "a")
		places = open(os.path.join(outPath, "total", "locations.csv"), "a")


		for tagged in st.tag(wordToke.tokenize(sourceText)):
			#print (tagged)
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