# -*- coding: utf-8 -*-

import urllib.request
import json
from bs4 import BeautifulSoup
import re

roomList = ["4F","6F", "7F", "8F", "9F", "コラボ1" , "コラボ5" , "コラボ6" , "コラボ7" , "コラボ機械室" , "コラボフロア"]

# url_base = "http://www2.jaist.ac.jp/cgi-local/room/searchresult?YEAR=2021&MONTH=11&DAY=01&WEEK=*"

month = input("月: ")
day = input("日: ")

if int(month) < 10:
    month = "0"+ month

if int(day) < 10:
    day = "0"+ day

year = "2021"

url = "http://www2.jaist.ac.jp/cgi-local/room/searchresult?YEAR=" + year + "&MONTH=" + month + "&DAY=" +day + "&WEEK=*"
# print(url)
# exit()

try:
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('shift-jis')
        soup = BeautifulSoup(text, "html.parser")
        wordclass = soup.find_all("th")
        wordlist = [x.text for x in wordclass]
        timer=[s for s in wordlist if re.search("\d\d:\d\d",s)]
        # print(timer)
        
        # for i in range(len(wordlist)):
        #     print(wordlist[i])
        # print(soup)

        for i in wordlist:
            if i in roomList:
                print(i)
            if re.search("\d\d:\d\d", i):
                print(i.lstrip('\n'))

except urllib.error.URLError as e:
    print(e.reason)