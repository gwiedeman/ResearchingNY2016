import json
import os

#for debugging
def pp(output):
	print (json.dumps(output, indent=2))
def serializeOutput(filename, output):
	__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
	f = open(os.path.join(__location__, filename + ".json"), "w")
	f.write(json.dumps(output, indent=2))
	f.close
	
input = open("ny19.json", "r")
text = input.read()
serializeOutput("ny19pp", text)
pp(text)