# HourlyBTC
BTC price graphing using plotly for a Telegram Channel

## Seting up the cronjobs

Its suggested that the generation of the graph, which is done by executing `genGraph.py` is set to a minute earlier to avoid conflicts.

3 cronjobs are needed for this to work as intended, to set up an hourly graph with updates on the text every ten minutes, the following cronjobs are needed:

`59 * * * * cd /directory/with/the/files/ && /usr/bin/python3.6 /directory/with/the/files/genGraph.py`

`0 * * * * cd /directory/with/the/files/ && /usr/bin/python3.6 /directory/with/the/files/renewGraph.py`

`10,20,30,40,50 * * * * cd /directory/with/the/files/ && /usr/bin/python3.6 /directory/with/the/files/renewText.py`

## 

Keep in mind that `renewGraph.py` will always send a new graph along with a message, so make sure you dont include a cronjob with `renewText.py` along with the one for `renewGraph.py`.
