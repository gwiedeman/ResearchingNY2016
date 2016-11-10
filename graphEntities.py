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

				issuePath = "/home/bcadmin/Projects/ResearchingNY2016/bdASP/ocrASP-bd"
				for issueFile in os.listdir(issuePath):
					issueNumber = issueFile.split(".")[0]
					newLine = {"year": issueNumber, "name": key, "value": 0}
					jsonData.append(newLine)


				for line in data:
					if "|" in line:
						entity = line.split("|")[0]
						fileName = line.split("|")[2]
						issue = fileName.split(".")[0]

						if entity.lower() == key.lower():
							for line in jsonData:
								if line["year"] == issue and line["name"] == key:
									line["value"] = line["value"] + 1

jsonText = json.dumps(jsonData)
f = open("graphData.json", "w")
f.write(jsonText)
f.close()