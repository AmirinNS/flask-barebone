import json

''' INIT '''
HOST, PORT = "", ""

# Replace some variable with setting.json
with open('settings.json') as settings:
	data = json.load(settings)
	HOST = data['host']
	PORT = data['port']
