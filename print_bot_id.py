#!/usr/bin/env python
import os
from slackclient import SlackClient

BOT_NAME='bixibot'

sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
	api_call = sc.api_call("users.list")

	if api_call.get('ok'):
		users = api_call.get('members')
		for user in users:
			if 'name' in user and user.get('name') == BOT_NAME:
				print("Bot ID for '%s' is %s"%(BOT_NAME, user.get('id')))
	else:
		print("NOT FOUND")
