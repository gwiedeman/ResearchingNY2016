import os
from mailbox import mbox
import html2text
from nltk.tag import StanfordNERTagger
from nltk.tokenize import TweetTokenizer, WordPunctTokenizer
import time
import json

startTime = time.time()
startTimeReadable = str(time.strftime("%Y-%m-%d %H:%M:%S"))
print ("Start Time: " + startTimeReadable)

__location__ = os.path.dirname(os.path.realpath(__file__))

senderJson = []

wordToke = WordPunctTokenizer()
stanfordPath = "/home/bcadmin/Projects/RNYImages/stanford-ner-2015-12-09"
st = StanfordNERTagger(os.path.join(stanfordPath, 'classifiers/english.all.3class.distsim.crf.ser.gz'), os.path.join(stanfordPath, 'stanford-ner-3.6.0.jar'))

outPath = os.path.join(__location__, "emailOut")
if not os.path.isdir(outPath):
	os.mkdir(outPath)

h = html2text.HTML2Text()
h.ignore_links = True
mboxDir = os.path.join(__location__, "Takeout", "Mail")

msgTotal = 0
for file in os.listdir(mboxDir):
	mboxPath = os.path.join(mboxDir, file)
	mboxObj = mbox(mboxPath)
	for message in mboxObj:
		msgTotal = msgTotal + 1

emailCount = 0
for file in os.listdir(mboxDir):
	mboxPath = os.path.join(mboxDir, file)
	mboxObj = mbox(mboxPath)
	for message in mboxObj:
		emailCount = emailCount + 1
		looptime = time.time()

		if 1 == 1:
			bodyText = ""
			sender = message['from']
			date = message['Date']

			senderMatch = False
			for person in senderJson:
				if person["name"] == sender:
					senderMatch = True
					person["value"] = person["value"] + 1
			if senderMatch == False:
				newLine = {"Sender": "Name", "name": sender, "value": 1}
				senderJson.append(newLine)

			subject = message['subject']
			if message.is_multipart():
				for part in message.walk():
					for subpart in part.walk():
						if subpart.get_content_type() == 'text/plain':
							bodyText = bodyText + str(subpart.get_payload(decode=True))
			else:
				for part in message.get_payload():
					bodyText = bodyText + part
			body = h.handle(bodyText)


			#totals
			orgs = open(os.path.join(outPath, "organizations.csv"), "a")
			peeps = open(os.path.join(outPath, "people.csv"), "a")
			places = open(os.path.join(outPath, "locations.csv"), "a")


			for tagged in st.tag(wordToke.tokenize(subject + "\n" + body)):
				#print (tagged)
				if tagged[1] == 'ORGANIZATION':
					orgs.write("\n" + tagged[0] + "|" + date + "|" + sender + "|" + subject)

				if tagged[1] == 'PERSON':
					peeps.write("\n" + tagged[0] + "|" + date + "|" + sender + "|" + subject)

				if tagged[1] == 'LOCATION':
					places.write("\n" + tagged[0] + "|" + date + "|" + sender + "|" + subject)

			orgs.close()
			peeps.close()
			places.close()



		processTime = time.time() - looptime
		totalTime = time.time() - startTime

		alert1 = "Process took " + str(processTime) + " seconds or " + str(processTime/60) + " minutes or " + str(processTime/3600) + " hours"
		avgTime = totalTime/emailCount
		alert2 = "Average time is " + str(avgTime)
		remaning = msgTotal - emailCount
		alert3 = str(remaning) + " Remaining"
		estimateTime = avgTime*remaning
		alert4 = "Estimated time left: " + str(estimateTime) + " seconds or " + str(estimateTime/60) + " minutes or " + str(estimateTime/3600) + " hours"
		print(alert1)
		print(alert2)
		print(alert3)
		print(alert4)

print(emailCount)

senderText = json.dumps(senderJson, indent=2)
f = open("senders.json", "w")
f.write(senderText)
f.close()