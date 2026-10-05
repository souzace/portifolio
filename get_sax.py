import urllib.request
import json
try:
    url = "https://raw.githubusercontent.com/Templarian/MaterialDesign/master/svg/saxophone.svg"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read().decode('utf-8')
    print(html)
except Exception as e:
    print(e)
