import re
import sys

import requests
from bs4 import BeautifulSoup

def send_telegram_message(bot_token, channel_name, message):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{bot_token}/sendMessage",
            data={
                'chat_id': channel_name,
                'text': message,
            },
        )
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending message: {e}")
        return None

def find_updates(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        text_content = soup.get_text()
        return re.findall(r"ECHO MINI (\S+) firmware changes", text_content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_env():
    config = {}
    with open(".env", "r") as f:
        for line in f.readlines():
            if "=" not in line:
                raise Exception("incorrect .env format")
            
            name, content = line.split("=", 1)
            config[name.strip()] = content.strip().replace('"', "")

    return config
        

if __name__ == "__main__":
    config = read_env()
    download_url = config["FIRMWARE_UPDATES_PAGE_URL"]
    versions = find_updates(download_url)
    if versions is None:
        print("Firmware versions are not found")
        sys.exit(1)

    versions = reversed(versions)
    try:
        with open("memory.txt", "r") as f:
            processed = [x.strip() for x in f.readline().split(",")]
    except FileNotFoundError:
        processed = []

    versions = list(filter(lambda x: x and x not in processed, versions))
    for version in versions:
        send_telegram_message(
            config["BOT_TOKEN"],
            config["TELEGRAM_CHANNEL_NAME"],
            f"🔥 New ECHO MINI Firmware update {version} 🔥\nDownload here: {download_url}", 
        )

    with open("memory.txt", "wt") as f:
        f.write(", ".join(processed + versions))

