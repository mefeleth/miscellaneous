import requests
import urllib.parse

# specify target url
response = requests.get("http://127.0.0.1/captcha")
# change the hidden input value accordingly
cut_string = str(response.content).split('value="')[1]
# change slice range accordingly
captcha = urllib.parse.quote_plus(cut_string[slice(0, 10, 1)])
print("CAPTCHA: " + captcha + "\n")
request2 = requests.get("http://127.0.0.1/captcha/submit?captcha="+captcha)
print(request2.content)
