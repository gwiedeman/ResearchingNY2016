from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer

wordToke = WordPunctTokenizer()
st = StanfordNERTagger(os.path.join(os.getcwd(), 'stanfordModel/classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(os.getcwd(), 'stanfordModel/stanford-ner-3.6.0.jar'))

for tagged in st.tag(wordToke.tokenize(sourceText)):
	print (tagged)
"""
	org = []
	person = []

	wasOrg = False
	wasPerson = False
	if tagged[1] == 'ORGANIZATION':
		csvrow['organization'] = tagged[0]
		wasOrg = True
		print wasOrg

	if tagged[1] == 'PERSON':
		csvrow['person'] = tagged[0]
		wasPerson = True
		print wasPerson

	if wasOrg or wasPerson:
		tweetWriter.writerow(csvrow)
print ('\n')
"""