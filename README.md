# slack-bixi-bot
A small slack bot to check the status of a given bixi status

In order for this to work, you must have 2 environment variables set:

One called `SLACK_BOT_TOKEN`, which you get from following the link [here](https://api.slack.com/bot-users).

Afterwards, you have to set `SLACK_BOT_ID`, which you get from running `print_bot_id.py`. You must change your bot name in `print_bot_id.py` before running it.

Lastly, you have to have find the bixi station id that you want (easier integration for this coming soon!)
