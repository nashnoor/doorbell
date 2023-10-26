import requests
requests.post("https://ntfy.sh/mytopic",
    data="Someone at the door😀".encode(encoding='utf-8'))
