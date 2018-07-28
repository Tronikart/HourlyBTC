import plotly.plotly as py
import plotly.graph_objs as go
import requests
import json

from datetime import datetime

key = 'KEY'
username = 'USERNAME'

py.sign_in(username, key)

now = datetime.now()

start_date = "2018-01-01"

url = "https://api.coindesk.com/v1/bpi/historical/close.json?start=" + start_date + "&end=" + now.strftime('%Y-%m-%d')

data = requests.get(url)
data = data.json()['bpi']

prices = []
dates = []

for key in data:
	dates.append(key)

dates.sort()
for key in dates:
	prices.append(data[key])

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

request = requests.get(url)
currentprice = request.json()['bpi']['USD']['rate_float']
prices[-1] = currentprice

layout = go.Layout(
	title='BTC Price History, ' + now.strftime('%Y-%m-%d, %I:%M %p') + ' (updated hourly)',
	plot_bgcolor='#424242',
	paper_bgcolor='#FF9900',
	showlegend=False,
	width=1920,
	titlefont=dict(
		family="Open Sans",
		size=30
	),
	height=1080,
	xaxis = dict(gridcolor='#bdbdbd'),
	yaxis = dict(
		gridcolor='#bdbdbd',
		autotick = False,
		ticks = 'outside',
		tick0 = prices[0],
		dtick = 1000
		),
	margin = go.Margin(
		l=60,
		r=40,
		b=30,
		t=70
	),
	annotations=[
		dict(
			visible=True,
			x=dates[-1],
			y=prices[-1],
			xref='x',
			yref='y',
			text="$" + str(prices[-1]),
			showarrow=True,
			font = dict(
				family="Open Sans",
				size=28,
				color="#ffffff"
			),
			align = 'center',
			arrowhead=2,
			arrowsize=1,
			arrowwidth=2,
			arrowcolor='#9E9E9E',
			ax=-200,
			ay=-100,
			bordercolor = '#9E9E9E',
			borderwidth = 1,
			borderpad = 2,
			bgcolor = '#BDBDBD',
			opacity=0.8
		)
	]
)


graph = [
go.Scatter(
	y=prices, 
	x=dates, 
	line = dict(
		color = '#FF9900'
	), 
	opacity = 0.8,
	name="",
	showlegend = False
),
go.Scatter(
	y=[prices[-1], prices[-1]],
	x=[dates[0], dates[-1]],
	line = dict(
		color = '#F44336'
	),
	opacity=1,
	mode='lines',
)]


py.image.save_as(dict(data=graph, layout=layout), filename='plot.png')