## APIs, WARCs, and NPL
#### technology, archives, and new opportunities for historical research

<br/>
<br/>
Gregory Wiedeman<br/>
University Archivist<br/>
M.E. Grenander Department of Special Collections & Archives<br/>
University at Albany, SUNY<br/>
@gregwiedeman

---

## Archives are changing

* Digitization and Born-digital archives
* More accessible research tools

* Access to archives is changing
	* Digitization on demand
	* Access though APIs
	* Emulation as a service
	
* More and More source material is becoming available for computational use


---

###  Research Tools Becoming More Accessible

* Becoming easier to use

* OCR
* APIs
* NLP
* Community-developed tools
	* Twac and Twarc reports
* Web Archiving
* Visualization tools

---
## Outline

* Show how easy these tools can be
* Point to real research
* Talk about archives and libraries support


---

## 19th Century Textbooks

* Widely used, copied & reprinted, relied upon for teaching

* John A. Nietz Collection at University of Pittsburgh
* Geography & World History texts with 5+ editions
* Blurry Pictures taken from digital camera in 2012

* Sections on Islamic World
	* Turkey in Europe
	* Asia (general sections)
	* Turkey in Asia
	* Persia
	* Arabia
	* Egypt
	* Barbary States

---

<!-- .slide: data-background="images/Morse1.jpg" -->
### Jedidiah Morse, 1826

---

<!-- .slide: data-background="images/Morse2.jpg" -->
### Jedidiah Morse, 1826

---

<!-- .slide: data-background="images/Willard.jpg" -->
### Emma Willard, 1835

---

<!-- .slide: data-background="images/Mitchell.jpg" -->
### S. Augustus Mitchell, 1847

---

<!-- .slide: data-background="images/Mitchell2.jpg" -->
### S. Augustus Mitchell, 1847

---
## Archives have Stuff

* Student Newspapers (1916-1985)
	* State College News
	* Albany Student Press (ASP)
* digitized from old microfilm
* already have high resolution TIFF masters

---
<!-- .slide: data-background="images/aspExample.png" -->

---

## Processing

* Changed to B&W and Greyscale with ImageMagik
	* Color was more successful anyway
* Python script with tesseract-ocr
	* os library to iterate thorugh images
	* subprocess library to call tesseract on each
	* write to text files
	* ASP took 11+ days
	
---

## Processing

~~~~
import os
from subprocess import Popen, PIPE

__location__ = os.path.dirname(os.path.realpath(__file__))

images = "C:\\Users\\Greg\\Pictures\\textbookPhotos"

for root, dirs, files in os.walk(images):
	for file in files:
		path = os.path.join(root, file)
		outpath = os.path.join(__location__, "ocr", os.path.basename(root))
		if not os.path.isdir(outpath):
			os.mkdir(outpath)

		process = Popen(['tesseract', path, os.path.join(outpath, file)], stdout=PIPE, stderr=PIPE)
		stdout, stderr = process.communicate()

~~~~

---

<!-- .slide: data-background="images/geoTextFiles.png" -->

---

<!-- .slide: data-background="images/textFiles.png" -->

---
## Terrible OCR
<!-- .slide: data-background="images/geoOCR.png" -->

---
## Okay OCR
<!-- .slide: data-background="images/ocrText.png" -->
---

## New Sources

* Collecting born-digital ASP since 2014
* Extract embeded text with mutool.exe

~~~~
import os
from subprocess import Popen, PIPE

__location__ = os.path.dirname(os.path.realpath(__file__))

for pdfFile in os.listdir(os.path.join(__location__, "pdf")):
	pdfPath = os.path.join(__location__, "pdf", pdfFile)
	outPath = os.path.join(__location__, "ocr", pdfFile.split("-")[1].split(".")[0] + ".txt")
	
	process = Popen(['C:\Program Files\mupdf\mutool.exe', 'draw', '-F', 'txt', '-o', outPath, pdfPath], stdout=PIPE, stderr=PIPE)
	stdout, stderr = process.communicate()
~~~~

---
<!-- .slide: data-background="images/bdASPExample.png" -->
---

## New Sources

~~~~

Celebrity clown or 
next president? PAGE 4

5 reasons 
Great  
Danes 
football 
will go 
undefeated 
this season. 
PAGE 10

MY INVOLVEMENTSUSTAINABILITY

T U E S D A Y ,  S E P T E M B E R  1 ,  2 0 1 5     I S S U E  1     A L B A N Y S T U D E N T P R E S S . N E T

P R I N T E D  B Y  T H E  T I M E S  U N I O N ,  A L B A N Y ,  N E W  Y O R K  —  A  H E A R S T  C O R P O R A T I O N  N E W S P A P E R

A L B A N Y  S T U D E N T  P R E S S

C E L E B R A T I N G  1 0 0  Y E A R S 
 1 9 1 6 — 2 0 1 6

By GRANT ZELIN
W 

ith climate change 
already affecting 
the world, the Uni-
versity at Albany is attempt-
ing to make a difference.
UAlbany introduced 
the Energy Campaign in 
the spring of 2007 as an 
electricity-saving competi-
tion among the six uptown 
residence halls. Now in its 
ninth year, the campaign is 
being expanded to include 
the Academic Podium and 
residential living areas.
Mary Ellen Mallia, the 
director for Environmental 
Sustainability, and Mary 
Alexis Leciejewski, the pro-
gram assistant for the Office 
of Environmental Sustain-
ability, hope to reduce elec-
tricity use the buildings the 
campaign is monitoring by 
10 percent from last year’s 
baseline.
While Mallia did admit 
that the goal is aggres-
sive, she also said that it is 
“completely realistic.” Last 
year the Energy Campaign 
attained an 8 percent reduc-
tion on campus. 
Eight percent may not 
sound like much, but each 
year the Energy Campaign 
saves around a million 
kilowatt-hours, or between 
$70,000 and $100,000 in 
electricity costs per year.
This year the Energy 
Campaign is pushing for 
joint action of students 
and staff to foster a more 

sustainable community 
at UAlbany. Residential 
Life has been increasing 
awareness of electrical 
waste, and it’s showing 
in the data. For example, 
Empire Commons and 
Freedom apartments 
have shown 30 percent 
reductions in electricity 
use over recent years. 
“It really is a focus 
on collective action,” 
Leciejewski said. “If you 
have faculty and staff 
setting the right example, 
the students who are 
working will carry those 
conservation habits with 
them for the rest of their 
life.”
~~~~

---

## Extract Entities

* Natural Language Processing
*  Stanford Corpus of Entities
*  Python nltk library
	* locations
	* people
	* organizations
	
<img src="images/tree.gif"/>

---
## NLP.py
~~~~
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



~~~~

---

<!-- .slide: data-background="images/csvOutput.png" -->

---

## makeCloud.py

~~~~
python3 makeCloud.py path/to/file.csv
~~~~

~~~~
import os
import sys
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

__location__ = os.path.dirname(os.path.realpath(__file__))

word_string = ""

if len(sys.argv) != 2:
	print ("Error: invalid arguments")
else:
	if os.path.isfile(sys.argv[1]):
		inputFile = sys.argv[1]
	else:
		inputFile = os.path.join(__location__, sys.argv[1])

	if not os.path.isfile(inputFile):
		print ("Error reading input file")
	else:
		file = open(inputFile, "r")
		data = file.readlines()
		file.close()


		for line in data:
			if "|" in line:
				word_string = word_string + " " + line.split("|")[0]

#from https://discuss.analyticsvidhya.com/t/how-can-i-create-word-cloud-in-python/969/2
wordcloud = WordCloud(font_path='/usr/share/fonts/truetype/freefont/FreeSans.ttf',
                          stopwords=STOPWORDS,
                          background_color='white',
                          width=1200,
                          height=1000
                         ).generate(word_string)


plt.imshow(wordcloud)
plt.axis('off')
plt.show()

~~~~

---

<!-- .slide: data-background="clouds/geoText-locations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Geography Texts - Locations</h3>

---

<!-- .slide: data-background="clouds/geoText-people.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Geography Texts - People</h3>
---

<!-- .slide: data-background="clouds/geoText-organizations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Geography Texts - Organizations</h3>
---

<!-- .slide: data-background="clouds/ocrASP-locations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Student Newspapers - Locations</h3>
---

<!-- .slide: data-background="clouds/ocrASP-people.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Student Newspapers - People</h3>
---

<!-- .slide: data-background="clouds/ocrASP-organizations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 100px">Student Newspapers - Organizations</h3>
---

<!-- .slide: data-background="clouds/bdASP-locations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Born-Digital ASP - Locations</h3>
---

<!-- .slide: data-background="clouds/bdASP-people.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Born-Digital ASP - People</h3>
---

<!-- .slide: data-background="clouds/bdASP-organizations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Born-Digital ASP - Organizations</h3>
---

### LOC's Chronicing America API

* Entire National Digital Newspaper Program is now accessible
* Millions of pages of OCR data
* Chronicling America Data Challenge winners
	* http://americaspublicbible.org/
	* http://www.americanlynchingdata.com/

---

<!-- .slide: data-background="clouds/bdASP-people.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 60px">Born-Digital ASP - Graphing Politicians</h3>
---

## Graph Entities

~~~~
python3 graphEntities.py bdASP/outASP-bd/total/people.csv Clinton Sanders Trump Obama Cruz
~~~~

~~~~

import os
import sys
import json

__location__ = os.path.dirname(os.path.realpath(__file__))

jsonData = []

if len(sys.argv) < 3:
	print ("Error: invalid arguments")
else:
	if os.path.isfile(sys.argv[1]):
		inputFile = sys.argv[1]
	else:
		inputFile = os.path.join(__location__, sys.argv[1])

	if not os.path.isfile(inputFile):
		print ("Error reading input file")
	else:
		keyCount = 0

		for key in sys.argv:
			keyCount = keyCount + 1
			if keyCount < 3:
				pass
			else:

				print ("Graphing " + key)

				file = open(inputFile, "r")
				data = file.readlines()
				file.close()

				issueList = ["2014_21", "2014_22", "2015_01", "2015_02","2015_03","2015_04","2015_05","2015_06","2015_07","2015_08","2015_09","2015_10","2015_12","2015_13","2015_14","2015_15","2015_16","2015_17","2015_18","2015_19","2015_20","2015_21","2015_22","2015_23", "2015_24"]
				for issueNumber in issueList:
					newLine = {"Issue": issueNumber, "name": key, "value": 0}
					jsonData.append(newLine)


				for line in data:
					if "|" in line:
						entity = line.split("|")[0]
						fileName = line.split("|")[2]
						issue = fileName.split(".")[0]
						if len(issue) == 6:
							issue = "_0".join(issue.split("_"))

						if entity.lower() == key.lower():
							for line in jsonData:
								if line["Issue"] == issue and line["name"] == key:
									line["value"] = line["value"] + 1

jsonText = json.dumps(jsonData, indent=2)
f = open("graphData.json", "w")
f.write(jsonText)
f.close()

~~~~


---
### D3plus

* Simple JS visualization Library

~~~~
<!doctype html>
<meta charset="utf-8">

<!-- load D3js -->
<script src="js/d3.js"></script>

<!-- load D3plus after D3js -->
<script src="js/d3plus.js"></script>

<!-- create container element for visualization -->
<div id="viz"></div>

<script>
  // sample data array
  var sample_data =   [
  {
    "value": 44,
    "name": "Clinton",
    "Issue": "2014_21"
  },
  {
    "value": 0,
    "name": "Clinton",
    "Issue": "2014_22"
  },
...
...
]
  // instantiate d3plus
  var visualization = d3plus.viz()
    .container("#viz")  // container DIV to hold the visualization
    .data(sample_data)  // data to use with the visualization
    .type("line")       // visualization type
    .id("name")         // key for which our data is unique on
    .text("name")       // key to use for display text
    .y("value")         // key to use for y-axis
    .x("Issue")          // key to use for x-axis
    .draw()             // finally, draw the visualization!
</script>

~~~~
* <a href="d3plus/graphASP.html">graphASP.html</a>
---

### Potiential of Born-digital

* Modern Political Archive - Experimental Email Archives
* Campaign Solicitation emails from New York State Federal Representatives
	* Collected with Gmail account 
	* June 23, 2016 - Election Day
	* 553 emails

---

## Processing

* used Python mailbox library to parse .mbox
* html2text library to convert html emails to plain text
* readEmail.py
	* iterate thorugh all emails, count unique senders
	* extract entities
* <a href="d3plus/emailSenders.html">D3plus bar graph to show senders</a>
* makeCloud.py for entities

---

<!-- .slide: data-background="clouds/email-locations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Email - Locations</h3>
---

<!-- .slide: data-background="clouds/email-people.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Email - People</h3>
---

<!-- .slide: data-background="clouds/email-organizations.png" -->
<h3 style="color: black; position:absolute; top: -350px; left: 150px">Email - Organizations</h3>
---

---

###What is the Role of Libraries and Archives?

* Potential of Communal Space
* History of Research Support

* Always-streached budgets
* Lack of expertise

---

What should Historians do?

* Look for grant funding
* Advocate for Institutional Support
* Build Connections