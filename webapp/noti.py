import requests
token = "<bot-token>"
url = f"https://api.telegram.org/bot{token}"
params = {"chat_id": "<your-id>", "text": "Someone at the door"}
r = requests.get(url + "/sendMessage", params=params)
