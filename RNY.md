## APIs, WARCs, and NPL
#### technology, archives, and new opportunities for historical research



Gregory Wiedeman

University Archivist

University at Albany, SUNY

---

##New Stuff

* Digitization
* Systems with open APIs

* New Communication Mediums
	* Digital files
	* Email
	* Web Archives
	* Application Data

	
---

# Moar Stuff


---

# New tools

* Becoming easier to use

* OCR
* APIs
* NLP
* Community-developed tools
	* Twac and Twarc reports
* Web Archiving


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

## Processing

* Changed to B&W and Greyscale with ImageMagik
	* Color was more successful
* Python script with tesseract
	* os library to iterate thorugh images
	* subprocess library to call tesseract on each
	* write to text files
	
---

## Processing

~~~~
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

~~~~


---
## Text


---

## Natural Language Toolkit (NLTK)

* Stanford Library


---

### Student Newspapers (1916-1985)

* Issues with extracting OCR text from Acrobat
* Python script tesseract 
* High Resolution TIFF Masters
	* 11+ days



---

### LOC's Chronicing America API


---

### Potiential of Born-digital

* MPA Experimental Email Archives



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