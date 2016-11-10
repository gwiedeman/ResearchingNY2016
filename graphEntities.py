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