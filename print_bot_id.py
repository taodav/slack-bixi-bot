#!/usr/bin/env python
from os.path import join, dirname
import os
from slackclient import SlackClient
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_NAME = os.environ.get('SLACK_BOT_NAME')

sc = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
	api_call = sc.api_call("users.list")

	if api_call.get('ok'):
		users = api_call.get('members')
		for user in users:
			if 'name' in user and user.get('name') == BOT_NAME:
				print("Bot ID for '%s' is %s"%(BOT_NAME, user.get('id')))
	else:
		print("API call failed")
