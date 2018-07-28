import requests
import json

token = 'TOKEN'
chanID = 'CHANNEL_ID'

def loadMessages():
	with open('messagesID.json') as f:
			post = json.load(f)
	return post

messages = loadMessages()

# delete minute stats
requests.get("https://api.telegram.org/bot" + token + "/deleteMessage?chat_id=" + chanID + "&message_id=" + str(messages['graph']))

# Sending Graph
url = "https://api.telegram.org/bot" + token + "/sendPhoto"
data = {'chat_id': chanID}
files = {'photo': open('plot.png', 'rb')}
request = requests.post(url, files=files, data=data)
messages['graph'] = request.json()['result']['message_id']

# Sending Text
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
request = requests.get(url)
data = request.json()
USD = data['bpi']['USD']['rate']
time = data['time']['updated']
output = "`1 BTC = $" + USD + "\n\n" + time + "`"
if request.status_code == requests.codes.ok:
	# delete graph
	requests.get("https://api.telegram.org/bot" + token + "/deleteMessage?chat_id=" + chanID + "&message_id=" + str(messages['stats']))
	request = requests.get("https://api.telegram.org/bot" + token + "/sendMessage?chat_id=" + chanID + "&text=" + output + "&parse_mode=Markdown")
	messages['stats'] = request.json()['result']['message_id']
else:
	pass

json.dump(messages, open('messagesID.json', 'w'))
