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