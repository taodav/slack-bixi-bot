#!/usr/bin/env python

from slackclient import SlackClient
import os
import pprint
import time
import requests

pp = pprint.PrettyPrinter(indent=4)

SLACK_TOKEN = os.environ.get("SLACK_BOT_TOKEN")
BOT_ID = os.environ.get("SLACK_BOT_ID")
BIXI_STATION_ID = 542

sc = SlackClient(SLACK_TOKEN)

def bixi_api_call():
	r = requests.get('https://secure.bixi.com/data/stations.json')
	stations = r.json().get('stations')
	if stations:
		for station in stations:
			if station.get('id') == BIXI_STATION_ID:
				return station
		return None

def parse_slack_output(slack_rtm_output):
	if slack_rtm_output and len(slack_rtm_output) > 0:
		#pp.pprint(slack_rtm_output)
		for output in slack_rtm_output:
			pp.pprint(output)
			if output and 'text' in output and output['type'] == 'message' and output['user'] != BOT_ID and 'bixi' in output['text']:
				return output['text'], output['channel']
	return (None, None)

def handle_command(command, channel):
	station_info = bixi_api_call();
	text = "Error: Could not find station!"
	if station_info:
		pp.pprint(station_info)
		text = "The de Gaspe/St-Viateur bixi station has %(ba)d bikes available and %(da)d docks available as of now." % station_info
	sc.api_call(
		"chat.postMessage",
		channel=channel,
		text=text,
		as_user=True
	)

if sc.rtm_connect():
	while True:
		command, channel = parse_slack_output(sc.rtm_read())
		if command and channel:
			handle_command(command, channel)
		time.sleep(1)
else:
	print "Connection failed"

