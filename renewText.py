import requests
import json

token = 'TOKEN'
chanID = 'CHANNEL_ID'
def loadMessages():
	with open('messagesID.json') as f:
			post = json.load(f)
	return post

messages = loadMessages()


url = "https://api.coindesk.com/v1/bpi/currentprice.json"
request = requests.get(url)
data = request.json()
USD = data['bpi']['USD']['rate']
time = data['time']['updated']
output = "`1 BTC = $" + USD + "\n\n" + time + "`"
request = requests.get("https://api.telegram.org/bot" + token + "/editMessageText?chat_id=" + chanID + "&message_id=" + str(messages['stats'])  + "&text=" + output + "&parse_mode=Markdown")
