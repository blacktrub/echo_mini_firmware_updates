# About the project

This is a simple script to check ECHO MINI Firmware update from their official page


## How to setup

The script is running in Python, so first of all we need to setup virtualenv:

```bash
$ python3 -m venv venv
```

Then install dependencies:

```bash
$ source venv/bin/activate
$ pip install -r req.txt
```

Put environment variables into .env file, e.g.:
```bash
BOT_TOKEN="your_telegra_bot_token"
TELEGRAM_CHANNEL_NAME="@your_telegram_channel_name"
FIRMWARE_UPDATES_PAGE_URL="https://forum.fiio.com/note/showNoteContent.do?id=202501210934383987154&tid=17"
```

You also need to add your bot as an admin to your channel, so it would have all rights to write messages


Now you can run the script:
```bash
$ source venv/bin/activate
$ python main.py
```

## Check the result

You can check out the result in my telegram channel: [t.me/echo_mini_firmware_updates](t.me/echo_mini_firmware_updates)

