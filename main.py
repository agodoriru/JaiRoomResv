# -*- coding: utf-8 -*-

import urllib.request
import json
from bs4 import BeautifulSoup

url = "http://www2.jaist.ac.jp/cgi-local/room/searchresult?YEAR=2021&MONTH=10&DAY=29&WEEK=fri"

try:
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('shift-jis')
        soup = BeautifulSoup(text, "html.parser")
        print(soup)

except urllib.error.URLError as e:
    print(e.reason)