import json

def spawn (mapName):
	with open('maps/'+mapName+'.map.json', 'r') as json_file:
		map = json.load(json_file)
	return map
